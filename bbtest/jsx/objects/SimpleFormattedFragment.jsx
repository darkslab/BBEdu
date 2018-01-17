function SimpleFormattedFragment(text) {
    const formats = [
        {
            regex: /\*{2}(?:(?:[^\s\*][^\*]*?[^\s\*])|[^\s\*])\*{2}/g,
            class: _BoldFormattedNestedSet
        },
        {
            regex: /~{2}(?:(?:[^\s~][^~]*?[^\s~])|[^\s~])~{2}/g,
            class: _ItalicFormattedNestedSet
        },
        {
            regex: /_{2}(?:(?:[^\s_][^_]*?[^\s_])|[^\s_])_{2}/g,
            class: _UnderlinedFormattedNestedSet
        }
    ];

    let contents = [];

    text = text.replace(/\r/g, "");
    text = $.trim(text);
    text = text.replace(/\n\s+\n/g, "\n\n");
    let paragraphs = text.split("\n\n");
    for (let i = 0; i < paragraphs.length; i++) {
        paragraphs[i] = $.trim(paragraphs[i]);
        let rootNestedSet = new _RootFormattedNestedSet(paragraphs[i], 0, paragraphs[i].length - 1);
        for (let j = 0; j < formats.length; j++) {
            let match;
            while (match = formats[j].regex.exec(paragraphs[i])) {
                let nestedSet = new formats[j].class(paragraphs[i], match.index, match.index + match[0].length - 1);
                if (rootNestedSet.canContain(nestedSet)) {
                    rootNestedSet.addSet(nestedSet);
                }
            }
        }
        contents.push(
            <React.Fragment key={i}>{rootNestedSet.content()}</React.Fragment>
        );
    }

    return (
        <React.Fragment>{contents}</React.Fragment>
    );
}


class _FormattedNestedSet {
    constructor(string, startPos, endPos) {
        this._string = string;
        this._start = startPos;
        this._end = endPos;
        this._innerSets = [];
    }
    start() {
        return this._start;
    }
    end() {
        return this._end;
    }
    content() {
        let ranges = [];
        ranges.push({
            start: this.start() + this.delimiterLength(),
            end: undefined
        });
        for (let i = 0; i < this._innerSets.length; i++) {
            ranges[ranges.length - 1].end = this._innerSets[i].start();
            ranges.push(this._innerSets[i]);
            ranges.push({
                start: this._innerSets[i].end() + 1,
                end: undefined
            });
            this._innerSets[i];
        }
        ranges[ranges.length - 1].end = this.end() - this.delimiterLength() + 1;

        let elems = [];
        for (let i = 0; i < ranges.length; i++) {
            if (ranges[i] instanceof _FormattedNestedSet) {
                elems.push(
                    <React.Fragment key={i}>{ranges[i].content()}</React.Fragment>
                );
            } else {
                let string = this._string.substring(ranges[i].start, ranges[i].end);
                if (string.length) {
                    let parts = string.split("  \n");
                    if (parts.length > 1) {
                        string = [];
                        let j = 0;
                        string.push(
                            <React.Fragment key={j++}>{parts.shift()}</React.Fragment>
                        );
                        let part;
                        while (part = parts.shift()) {
                            string.push(
                                <React.Fragment key={j++}><br /></React.Fragment>
                            );
                            string.push(
                                <React.Fragment key={j++}>{part}</React.Fragment>
                            );
                        }
                    }
                    elems.push(
                        <React.Fragment key={i}>{string}</React.Fragment>
                    );
                }
            }
        }

        let Tag = this.tag();
        return (
            <Tag>{elems}</Tag>
        );
    }
    canContain(nestedSet) {
        return this.start() < nestedSet.start() && nestedSet.end() < this.end();
    }
    addSet(nestedSet) {
        for (let i = 0; i < this._innerSets.length; i++) {
            if (this._innerSets[i].canContain(nestedSet)) {
                this._innerSets[i].addSet(nestedSet);
                return;
            }
        }

        let deferredSets = [];
        let leftInnerSets = [];
        for (let i = 0; i < this._innerSets.length; i++) {
            if (nestedSet.canContain(this._innerSets[i])) {
                deferredSets.push(this._innerSets[i]);
            } else {
                leftInnerSets.push(this._innerSets[i]);
            }
        }
        if (deferredSets.length) {
            leftInnerSets.push(nestedSet);
            this._sortNestedSets(leftInnerSets);
            if (this._doOrderedSetsOverlap(leftInnerSets)) {
                return;
            }
            this._innerSets = leftInnerSets;
            for (let i = 0; i < deferredSets.length; i++) {
                nestedSet.addSet(deferredSets[i]);
            }
            return;
        }

        let newInnerSets = this._innerSets.slice();
        newInnerSets.push(nestedSet);
        this._sortNestedSets(newInnerSets);
        if (this._doOrderedSetsOverlap(newInnerSets)) {
            return;
        }

        this._innerSets = newInnerSets;
    }

    _doOrderedSetsOverlap(nestedSets) {
        if (!nestedSets.length) {
            return false;
        }
        for (let lastSet = nestedSets[0], i = 1; i < nestedSets.length; lastSet = nestedSets[i++]) {
            if (nestedSets[i].start() <= lastSet.end()) {
                return true;
            }
        }
        return false;
    }
    _sortNestedSets(nestedSets) {
        nestedSets.sort((a, b) => {
            if (a.start() === b.start()) {
                return 0;
            }
            return a.start() < b.start() ? -1 : 1;
        });
    }
}

class _RootFormattedNestedSet extends _FormattedNestedSet {
    canContain(nestedSet) {
        return true;
    }
    tag() {
        return "p";
    }
    delimiterLength() {
        return 0;
    }
}

class _BoldFormattedNestedSet extends _FormattedNestedSet {
    tag() {
        return "strong";
    }
    delimiterLength() {
        return 2;
    }
}

class _ItalicFormattedNestedSet extends _FormattedNestedSet {
    tag() {
        return "em";
    }
    delimiterLength() {
        return 2;
    }
}

class _UnderlinedFormattedNestedSet extends _FormattedNestedSet {
    tag() {
        return "u";
    }
    delimiterLength() {
        return 2;
    }
}
