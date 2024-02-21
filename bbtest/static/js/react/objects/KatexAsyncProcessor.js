"use strict";

function _typeof(o) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (o) { return typeof o; } : function (o) { return o && "function" == typeof Symbol && o.constructor === Symbol && o !== Symbol.prototype ? "symbol" : typeof o; }, _typeof(o); }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, _toPropertyKey(descriptor.key), descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
function _toPropertyKey(arg) { var key = _toPrimitive(arg, "string"); return _typeof(key) === "symbol" ? key : String(key); }
function _toPrimitive(input, hint) { if (_typeof(input) !== "object" || input === null) return input; var prim = input[Symbol.toPrimitive]; if (prim !== undefined) { var res = prim.call(input, hint || "default"); if (_typeof(res) !== "object") return res; throw new TypeError("@@toPrimitive must return a primitive value."); } return (hint === "string" ? String : Number)(input); }
var KatexAsyncProcessor = /*#__PURE__*/function () {
  function KatexAsyncProcessor(callback, text) {
    _classCallCheck(this, KatexAsyncProcessor);
    this._callback = callback;
    this._originalText = text;
    this._isActive = true;
    this._$container = $("<div></div>");
    ReactDOM.render(SimpleFormattedFragment(this._originalText), this._$container[0], this._doneRendering.bind(this));
  }
  _createClass(KatexAsyncProcessor, [{
    key: "stop",
    value: function stop() {
      this._isActive = false;
    }
  }, {
    key: "_doneRendering",
    value: function _doneRendering() {
      if (!this._isActive) {
        return;
      }
      renderMathInElement(this._$container[0], {
        throwOnError: false,
        delimiters: [{
          left: "$$",
          right: "$$",
          display: true
        }, {
          left: "$",
          right: "$",
          display: false
        }]
      });
      this._callback(this._$container.html(), this._originalText);
    }
  }]);
  return KatexAsyncProcessor;
}();
function _load_calculator() {
  // Get placement
  var queryString = window.location.search;
  // console.log(queryString);
  var urlParams = new URLSearchParams(queryString);
  var placementUrlParam = urlParams.get('placement');
  // console.log(placementUrlParam);

  // const placement =  placementUrlParam || 'auto'

  var placement = "bottom";
  // console.log(placement);

  // configure the default type of number as BigNumbers
  math.config({
    number: 'BigNumber',
    // Default type of number use bignumber!  test with 666%10:
    // 	'number' (default), 'bignumber', or 'fraction'
    precision: 20 // Number of significant digits for BigNumbers
  });

  if (!math.percent) {
    math.percent = function (x, y) {
      return y / x * 100;
    };
  }
  function sendMessage(display) {
    if (parent.postMessage) {
      parent.postMessage(display, '*');
    }
  }
  $('[data-calculator]').on('show.bs.popover', function () {
    sendMessage("show");
  });
  $('[data-calculator]').on('hide.bs.popover', function () {
    sendMessage("hide");
  });

  // <a class="function-button percent" href="#">%</a>\
  // <a class="modifier-button squareroot" href="#">&#8730;</a>\
  // <a class="modifier-button plusminus" href="#">&#0177;</a>\

  $('[data-calculator]').popover({
    html: true,
    animation: true,
    content: function content() {
      var html = '<div id="calculator">\
                    <div id="display" class="pull-right" contenteditable="true"></div>\
                    <a class="clear-button clear" href="#">C</a>\
                    <div id="statusContainer">\
                        <div id="status" class="pull-right"></div>\
                    </div>\
                    <a class="num-button seven" href="#">7</a>\
                    <a class="num-button eight" href="#">8</a>\
                    <a class="num-button nine" href="#">9</a>\
                    <a class="num-button four" href="#">4</a>\
                    <a class="num-button five" href="#">5</a>\
                    <a class="num-button six" href="#">6</a>\
                    <a class="num-button one" href="#">1</a>\
                    <a class="num-button two" href="#">2</a>\
                    <a class="num-button three" href="#">3</a>\
                    <a class="num-button zero" href="#">0</a> \
                    <a class="num-button dot" href="#">.</a>\
                    <a class="clear-button clear" href="#">C</a>\
                    <a class="function-button add" href="#">+</a>\
                    <a class="function-button subtract" href="#">&ndash;</a>\
                    <a class="function-button multiply" href="#">&#0215;</a>\
                    <a class="function-button divide" href="#">&#0247;</a>\
                    <a class="equals-button" href="#">=</a>\
                    <div id="calculatorFooter"></div>\
                </div>';
      return html;
    },
    placement: placement
  }).on('hidden.bs.popover', function (e) {}).on('shown.bs.popover', function () {
    Calculator.init(); //Build calculator
  });

  var Calculator = {
    init: function init() {
      var $display = $("#display");
      var $status = $("#status");
      var finalValueS = '0';
      var ctrlDown = false;
      var shiftDown = false;
      var ctrlKey = 17,
        shiftKey = 16,
        vKey = 86,
        cKey = 67;
      $display.on('keydown', function (e) {
        console.log(e.keyCode);
        e.preventDefault();
        try {
          switch (e.keyCode) {
            case 39:
              //$display.animate({scrollLeft: '+=50' }, 100)
              var caretPos = getCaretCharacterOffsetWithin(document.getElementById("display"));
              var offset = caretPos + 1;
              if (offset <= $display.text().length) setCaretPos("display", offset);
              break;
            case 37:
              var caretPos = getCaretCharacterOffsetWithin(document.getElementById("display"));
              var offset = caretPos - 1;
              if (offset >= 0) setCaretPos("display", offset);
              //$display.animate({scrollLeft: '-=50' }, 100)
              break;
            case ctrlKey:
              ctrlDown = true;
              break;
            case shiftKey:
              shiftDown = true;
              console.log(shiftDown);
              break;
          }
        } catch (e) {}
      }).keyup(function (e) {
        if (e.keyCode == ctrlKey) ctrlDown = false;
        if (e.keyCode == shiftKey) shiftDown = false;
      });
      var tooltipText = 'LinangData';
      var html = '<a id="linangdata" href="#" data-placement="top" data-toggle="tooltip" href="#" data-original-title="' + tooltipText + '"></a>';
      $('#calculatorFooter').html(html);
      $('a').tooltip();
      function keyDownFromString(computeString) {
        //Handle paste here - allowed values only
        //parse string and fire keydown events...
        var keymap = [];
        keymap['0'] = 48;
        keymap['1'] = 49;
        keymap['2'] = 50;
        keymap['3'] = 51;
        keymap['4'] = 52;
        keymap['5'] = 53;
        keymap['6'] = 54;
        keymap['7'] = 55;
        keymap['8'] = 56;
        keymap['9'] = 57;
        keymap['x'] = 106;
        keymap["\xD7"] = 106;
        keymap['/'] = 111;
        keymap["\xF7"] = 111;
        keymap['+'] = 107;
        keymap['-'] = 109;
        keymap["\u2013"] = 109;
        keymap['.'] = 110;
        keymap['%'] = 112;
        keymap["\u221A"] = 113; //√
        keymap["\xB1"] = 114; //±

        for (var i = 0; i < computeString.length; i++) {
          var keyPasted = keymap[computeString[i]];
          //console.log(data[i])
          //console.log( keyPasted );
          if (_typeof(keyPasted) !== undefined) {
            var e = $.Event('keydown');
            e.which = keyPasted;
            $("#calculator").trigger(e);
          }
        }
      }
      $(".equals-button").focus();
      $("#calculator").unbind().on('keydown', function (e) {
        //$(document).unbind().on('keydown', function(e) {
        e.preventDefault();
        e.stopPropagation();

        //console.log(e);
        //console.log(e.which);
        //switch ( e.keyCode ) {
        switch (e.which) {
          case 13:
            //Enter key
            $(".equals-button").trigger("click");
            break;
          case 187:
            //console.log("enter")
            //console.trace()
            if (shiftDown) $(".add").trigger("click");else $(".equals-button").trigger("click");
            break;
          case ctrlKey:
            ctrlDown = true;
            break;
          case shiftKey:
            shiftDown = true;
            break;
          case 106: //Multiply
          case 88:
            //case 56:  
            $(".multiply").trigger("click");
            break;
          case 111: //Divide
          case 191:
            //case 47:
            $(".divide").trigger("click");
            break;
          case 107:
            //plus
            //case 43:	
            $(".add").trigger("click");
            break;
          case 109: //minus
          case 189:
            $(".subtract").trigger("click");
            break;
          case 110:
          case 190:
            $(".dot").trigger("click");
            break;
          case 96:
          case 48:
            $(".zero").trigger("click");
            break;
          case 97:
          case 49:
            $(".one").trigger("click");
            break;
          case 98:
          case 50:
            $(".two").trigger("click");
            break;
          case 99:
          case 51:
            $(".three").trigger("click");
            break;
          case 100:
          case 52:
            $(".four").trigger("click");
            break;
          case 101:
          case 53:
            if (shiftDown) $(".percent").trigger("click");else $(".five").trigger("click");
            break;
          case 102:
          case 54:
            $(".six").trigger("click");
            break;
          case 103:
          case 55:
            $(".seven").trigger("click");
            break;
          case 104:
          case 56:
            if (shiftDown) $(".multiply").trigger("click");else $(".eight").trigger("click");
            break;
          case 105:
          case 57:
            $(".nine").trigger("click");
            break;
          case 112:
            //% percent
            $(".percent").trigger("click");
            break;
          case 113:
            //sqrt
            $(".squareroot").trigger("click");
            break;
          case 114:
            //plusminus
            $(".plusminus").trigger("click");
            break;
          case 8:
            //Backspace
            var caretPos = getCaretCharacterOffsetWithin(document.getElementById("display"));
            var newString = $display.text().removeAt(caretPos - 1, "");
            $(".clear-button").trigger('click');
            keyDownFromString(newString);
            if (caretPos - 1 >= 0) setCaretPos("display", caretPos - 1);
            break;
          case 46:
            // del
            var caretPos = getCaretCharacterOffsetWithin(document.getElementById("display"));
            setCaretPos("display", caretPos);
            var newString = $display.text().removeAt(caretPos, "");
            $(".clear-button").trigger('click');
            keyDownFromString(newString);
            if (caretPos >= 0) setCaretPos("display", caretPos);
            break;
          case 67:
            //letter c - copy/clear	
            if (ctrlDown) {
              try {
                var successful = document.execCommand('copy');
                var msg = successful ? 'successful' : 'unsuccessful';
                console.log('Copying text command was ' + msg);
              } catch (err) {
                //console.log('Oops, unable to copy');
              }
            } else {
              $(".clear-button").trigger('click');
            }
            break;
          default:
            //console.log("default")
            break;
        }
      }).keyup(function (e) {
        if (e.keyCode == ctrlKey) ctrlDown = false;
        if (e.keyCode == shiftKey) shiftDown = false;
      });
      ;
      function getLastState() {
        // Retrieve the object from storage
        var calculatorState = localStorage.getItem('calculatorState');
        if (calculatorState) {
          //console.log('calculatorState: ', JSON.parse(calculatorState));		
          var result = $.parseJSON(calculatorState);
          $.each(result, function (k, v) {
            //display the key and value pair
            //console.log(k + ' is ' + v);
            v = typeof v !== "undefined" ? v : "";
            if (k == "display") {
              $display.text(v);
            } else if (k == "number") {
              v !== "" ? $display.data("number", v) : $display.data("number", 0);
            } else if (k == "status") {
              $status.text(v);
            } else if (k == "finalValueS") {
              finalValueS = v !== "" ? v : 0;
            } else {
              $display.data(k, v);
            }
          });
        } else {
          resetCalc(0);
          $status.text("");
          $display.text(0);
        }
        //list local storage variables
        //for (var i = 0; i < localStorage.length; i++) {
        //  console.log(localStorage.key(i))
        //};
        //console.log(localStorage)	
      }
      ;
      function setLastState() {
        var calculatorState = {
          'fromPrevious': $display.data("fromPrevious"),
          'isFunctionPending': $display.data("isFunctionPending"),
          'number': $display.data("number"),
          'status': $status.text(),
          'display': $display.text(),
          'finalValueS': finalValueS
        };
        //console.log(localStorage)
        // Put the object into storage
        localStorage.setItem('calculatorState', JSON.stringify(calculatorState));
        debugValues();
      }
      ;

      //console.log("Dev.");
      getLastState();
      $(".num-button").click(function (e) {
        e.preventDefault();
        e.stopPropagation();
        var number = $(this).text();
        if (number == ".") {
          if ($display.text().searchTest("\\.$")) return;
        }
        if ($display.data("fromPrevious")) {
          //After a calculation has just been performed.
          //	-  Reset the calculator to new number.	
          resetCalc(number);
          finalValueS = number;

          //var display = $display.text()
          //animateItem($status, "Ans = " + display, true)
          //animateItem($display, number, false)

          $status.text("Ans = " + $display.text());
          $display.text(number);

          //	After a function button has just been selected.
          //		- Lock the first number, replace the display with the new number.
        } else if ($display.data("isFunctionPending")) {
          finalValueS += number;
          $display.data("number", number);
          $display.text($display.text() + number);
          $display.data("isFunctionPending", false);

          // In a totally fresh state (display shows zero)
          //	- Append the new number to what is already there. If it's a zero, replace that. 	
        } else {
          var curValue = $display.data("number");
          var toAdd = number;
          if (curValue == "0") {
            curValue = "";
            $display.text(toAdd);
            finalValueS = toAdd;
          } else {
            $display.text($display.text() + toAdd);
            finalValueS += toAdd;
          }
          var newValue = curValue + toAdd;
          $display.data("number", newValue);
          //$display.text(newValue);
        }

        setLastState();
      });
      $(".modifier-button").click(function (e) {
        e.preventDefault();
        if ($display.data("fromPrevious")) {
          finalValueS = $display.data("number");
          resetCalc(finalValueS);

          //var display = $display.text()
          //animateItem($status, "Ans: " + display, true)
          //animateItem($display, finalValueS, false)

          $status.text("Ans = " + $display.text());
          $display.text(finalValueS);
        }
        try {
          //Handle single function keys like square root - i.e., treat as a modifier for the digit shown in display
          var modValue = 0;
          var number = $display.data("number").toString();
          if (number != "") {
            if ($(this).text() == "\u221A") {
              // Square root
              //if ( number >= 0) {							
              modValue = math.eval('sqrt(' + number + ')');
              $display.text($display.text() + "\u221A");
              var finalValueTmp = finalValueS.toString();
              finalValueS = finalValueTmp.searchReplace(number + '$', modValue);

              //} else {  //Can't do sqrt of minus
              // return;
              //}
            } else if ($(this).text() == "\xB1") {
              // Plus minus 177
              if (number >= 0) {
                modValue = -Math.abs(number);
                var newStatus = $display.text();
                newStatus = newStatus.searchReplace(number + '$', modValue);
                $display.text(newStatus);
                var finalValueTmp = finalValueS.toString();
                finalValueS = finalValueTmp.searchReplace(number + '$', modValue);
              } else {
                modValue = Math.abs($display.data("number"));
                var newStatus = $display.text();
                newStatus = newStatus.searchReplace(number + '$', modValue);
                $display.text(newStatus);
                var finalValueTmp = finalValueS.toString();
                finalValueS = finalValueTmp.searchReplace(number + '$', modValue);
                //console.log("modValue: " + modValue)
              }
            }
            //console.log("finalValueS: " + finalValueS)
            //finalValue = parseFloat( finalValue.toFixed(14) )
            $display.data("number", modValue.toString());
          }
        } catch (e) {
          console.log(finalValueS);
          console.log(e);
        }
        setLastState();
      });
      $(".function-button").click(function (e) {
        e.preventDefault();
        e.stopPropagation();
        if ($display.data("fromPrevious")) {
          finalValueS = $display.data("number");
          resetCalc(finalValueS);

          //var display = $display.text()
          //animateItem($status, "Ans: " + display, true)
          //animateItem($display, finalValueS, false)	

          $status.text("Ans = " + $display.text());
          $display.text(finalValueS);
        }

        // Function selected
        var pendingFunction = $(this).text();
        var number = $display.text().toString();
        if (!$display.data("isFunctionPending")) {
          if (pendingFunction == "+") {
            $display.text(number + pendingFunction);
            finalValueS += "+";
          } else if (pendingFunction == "\u2013") {
            //2013 ndash
            $display.text(number + "-");
            finalValueS += "-";
          } else if (pendingFunction == "\xD7") {
            //0215 x Times 
            $display.text(number + pendingFunction);
            finalValueS += "*";
          } else if (pendingFunction == "\xF7") {
            //0247 Divide
            $display.text(number + pendingFunction);
            finalValueS += "/";
          } else if (pendingFunction == "%") {
            // 
            $display.text(number + pendingFunction);
            finalValueS += "%";
          }
          $display.data("isFunctionPending", true);
        } else {
          if (pendingFunction == "\u2013") {
            //minus
            number = number.searchReplace("--", "-");
            $display.text(number + "-");
            finalValueS += "-";
          }
        }
        setLastState();
      });
      $(".equals-button").click(function (e) {
        e.preventDefault();
        e.stopPropagation();
        try {
          //Parse status field for calculation.
          //modify finalValueS to catch any % functions  
          var finalValueTmp = finalValueS.toString();
          finalValueS = finalValueTmp.searchReplace("([0-9\.]+)%([0-9\.]+)", "($2/100)*$1"); //Binary percentage function
          finalValueS = finalValueS.searchReplace("(.*?)([\+-\/\*])([0-9\.]+)%$", "($1)$2(($3/100)*($1))"); //Unary percentage function

          //console.log(finalValueS)
          var finalValue = math.eval(finalValueS).toString();
          //console.log(finalValue)			

          if (typeof finalValue !== "undefined") {
            $display.data("number", finalValue);
            var display = $display.text();
            animateItem($status, display + "=", true);
            animateItem($display, finalValue, true);
            resetCalc(finalValue);
            $display.data("fromPrevious", true);
            setLastState();
          } else {
            console.log('finalValue undefined');
          }
        } catch (e) {
          //fail quietly
          console.log(finalValueS);
          console.log(e);
        }
      });
      $(".clear-button").click(function (e) {
        //console.log(e)
        e.preventDefault();
        e.stopPropagation();
        resetCalc(0);
        $display.text(0);
        $status.text("");
        finalValueS = "0";
        setLastState();
      });
      function animateItem($ele, val, text) {
        $ele.animate({
          'opacity': 0
        }, 120, function () {
          if (text) $(this).text(val);else $(this).val(val);
          setLastState();
        }).animate({
          'opacity': 1
        }, 120);
      }
      function resetCalc(curValue) {
        //console.log( "resetCalc: " + curValue);
        //console.trace()
        $display.data("number", curValue);
        $display.data("isFunctionPending", false);
        $display.data("fromPrevious", false);
      }
      $status.on('keydown', function (e) {
        //console.log(e)
        switch (e.keyCode) {
          case 39:
            $status.animate({
              scrollLeft: '+=50'
            }, 100);
            break;
          case 37:
            $status.animate({
              scrollLeft: '+=50'
            }, 100);
            break;
        }
      });
      function debugValues() {
        return;
        console.log("isFunctionPending: " + $display.data("isFunctionPending"));
        console.log("fromPrevious: " + $display.data("fromPrevious"));
        console.log("number: " + $display.data("number"));
        console.log("finalValueS: " + finalValueS);
        console.log("Display Text: " + $display.text());
      }
      function getCaretCharacterOffsetWithin(element) {
        var caretOffset = 0;
        if (typeof window.getSelection != "undefined") {
          var range = window.getSelection().getRangeAt(0);
          var preCaretRange = range.cloneRange();
          preCaretRange.selectNodeContents(element);
          preCaretRange.setEnd(range.endContainer, range.endOffset);
          caretOffset = preCaretRange.toString().length;
        } else if (typeof document.selection != "undefined" && document.selection.type != "Control") {
          var textRange = document.selection.createRange();
          var preCaretTextRange = document.body.createTextRange();
          preCaretTextRange.moveToElementText(element);
          preCaretTextRange.setEndPoint("EndToEnd", textRange);
          caretOffset = preCaretTextRange.text.length;
        }
        return caretOffset;
      }
      function showCaretPos(ele) {
        console.log("Caret position: " + getCaretCharacterOffsetWithin(document.getElementById(elem)));
      }
      function setCaretPos(ele, pos) {
        try {
          var el = document.getElementById(ele);
          var range = document.createRange();
          var sel = window.getSelection();
          range.setStart(el.childNodes[0], pos);
          range.collapse(true);
          sel.removeAllRanges();
          sel.addRange(range);
        } catch (e) {}
      }
      String.prototype.searchReplace = function (searchForStr, replaceWithStr) {
        return this.replace(new RegExp(searchForStr, "igm"), replaceWithStr);
      };
      String.prototype.searchTest = function (searchPattern) {
        var patt = new RegExp(searchPattern);
        return patt.test(this);
      };
      String.prototype.replaceAt = function (index, character) {
        return this.substr(0, index) + character + this.substr(index + character.length);
      };
      String.prototype.removeAt = function (index) {
        return this.substr(0, index) + this.substr(index + 1);
      };
      if (!String.prototype.splice) {
        /**
         * {JSDoc}
         *
         * The splice() method changes the content of a string by removing a range of
         * characters and/or adding new characters.
         *
         * @this {String}
         * @param {number} start Index at which to start changing the string.
         * @param {number} delCount An integer indicating the number of old chars to remove.
         * @param {string} newSubStr The String that is spliced in.
         * @return {string} A new string with the spliced substring.
         */
        String.prototype.splice = function (start, delCount, newSubStr) {
          return this.slice(0, start) + newSubStr + this.slice(start + Math.abs(delCount));
        };
      }

      // $("#linangdata").click(function () {
      // 	window.open("https://linangdata.com", "_blank");
      // });
    }
  };
}

function _unload_calculator() {
  $('[data-calculator]').off();
  // $('[data-calculator]').off('hide.bs.popover')
}