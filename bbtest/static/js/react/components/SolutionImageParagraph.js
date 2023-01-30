"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var SolutionImageParagraph = function (_React$Component) {
    _inherits(SolutionImageParagraph, _React$Component);

    function SolutionImageParagraph(props) {
        _classCallCheck(this, SolutionImageParagraph);

        return _possibleConstructorReturn(this, (SolutionImageParagraph.__proto__ || Object.getPrototypeOf(SolutionImageParagraph)).call(this, props));
    }

    _createClass(SolutionImageParagraph, [{
        key: "render",
        value: function render() {
            var className = "bb-test-paragraph";
            var imgClassName = void 0;
            var imgSrc = void 0;
            if (this.props.data.asset_url) {
                imgClassName = "img-responsive center-block bb-test-paragraph-image";
                imgSrc = this.props.data.asset_url;
            } else {
                className += " bb-test-paragraph-image-waiting";
                imgClassName = "bb-spinner";
                imgSrc = this.props.data.spinner_logo_url;
            }

            return React.createElement(
                "div",
                { className: className },
                React.createElement("img", { className: imgClassName, src: imgSrc })
            );
        }
    }]);

    return SolutionImageParagraph;
}(React.Component);