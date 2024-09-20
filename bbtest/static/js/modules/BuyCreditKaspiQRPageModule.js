BuyCreditKaspiQRPageModule.prototype = Object.create(Module.prototype);
function BuyCreditKaspiQRPageModule() {
    this._$form = $("[data-kaspi-qr-form]");
    console.log(this._$form)
    console.log(this._$form.find('input[name="payment_url"]').val())

    if (this._$form.length) {
        // this._$form.submit();
        const kaspi_link = this._$form.find('input[name="payment_url"]').val()
        
        var isMobile = window.matchMedia("(any-pointer:coarse)").matches | window.innerWidth <= 768;
        if (isMobile) {
            // Create the button element
            // var mobileButton = document.createElement("button");
            // mobileButton.type = "button";
            // mobileButton.id = "kaspi-redirect-button";
            // mobileButton.className = "btn btn-primary";
            // mobileButton.innerHTML = "Оплатить в приложении";
            // mobileButton.onclick = function() {
            //     location.href = '{{ payment_url }}';
            // };

            // // Find the block_footer element and insert the button after it
            // var blockFooter = document.querySelector(".block_footer");
            // if (blockFooter) {
            //     blockFooter.parentNode.insertBefore(mobileButton, blockFooter.nextSibling);
            // }
            window.location.href = kaspi_link
        
        } else {
            // setTimeout(() => { window.location.href = "../"}, 0.1*60*1000)
        }


        // window.location.href = kaspi_link;
        // window.open(kaspi_link, '_blank');
    }

    Module.call(this);
}
BuyCreditKaspiQRPageModule.prototype.unMount = function() {
}
