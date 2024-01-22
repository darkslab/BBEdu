
setIframeSize = function(size) {
    //$('#linangcalc').css('width', size.width );
    //$('#linangcalc').css('height', size.height );
    document.getElementById("linangcalc").width = size.width;
    document.getElementById("linangcalc").height = size.height;
}

window.addEventListener('message', function(event) {
 // console.log('event', event.data)
  if ( event.data == "hide") 
      setIframeSize({"width":50, "height":50});
  else if (event.data == "show") 
      setIframeSize({"width":380, "height":350});
});

