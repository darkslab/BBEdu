SuperCreateStudentsModule.prototype = Object.create(Module.prototype);
function SuperCreateStudentsModule() {
    this._$form = $("[data-create-students-form]");
    this._$createStudentConfirmButtons = $("[data-create-students-confirm]");
    
    this.form_name = $("#id_name");
    this.form_prefix = $("#id_prefix");
    this.form_amount = $("#id_amount");

    this.confirm_create_button = $("#confirm-create");
    console.log(this.confirm_create_button);
    this.confirm_create_button.on("click", function() {
        console.log(this.confirm_create_button);
        $('#StudentModal').modal('hide');
        return false;
    });

    this._boundUpdateFormAction = this._updateFormAction.bind(this);
    this._updatePreviewBind = this.updatePreview.bind(this);

    this._$createStudentConfirmButtons.on("click", this._boundUpdateFormAction);

    // dynamic preview when values in form are changing
    this.form_prefix.keyup(this._updatePreviewBind);
    this.form_amount.keyup(this._updatePreviewBind);
    this.form_name.keyup(this._updatePreviewBind);
    this.form_amount.on("change", this._updatePreviewBind);
    
    // $.fileDownload('export.csv').done(function () { console.log("asd") });


    Module.call(this);
    this.updatePreview();
}
SuperCreateStudentsModule.prototype.unMount = function() {
    this._$createStudentConfirmButtons.off("click", this._boundUpdateFormAction);
}
SuperCreateStudentsModule.prototype._updateFormAction = function(event) {
    var $button = $(event.currentTarget);
    console.log("print");
    if (!$button.data("create-students-confirm")) {
        return;
    }
    // this._$createStudentConfirmButtons.attr("disabled", true);
    this._$form.submit();
    $('#modal-asd').modal('toggle');
    // window.location.href = "/super/users/";
}
SuperCreateStudentsModule.prototype.updatePreview = function(){
    var amount = this.form_amount.val();
    var prefix = this.form_prefix.val();
    var name = this.form_name.val();
    var preview = "";

    if (amount == ""){
        $('#preview-dynamyc-table').find("tr:gt(0)").remove();
        return;
    }else if(amount > 20){
        amount = 20;
    }
    if(name == "") {
        name = "Student Iqanat";
    }

    for (let i = 1; i <= amount; i++) {
        var rnd = Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 10);
        var email = prefix + "_" + rnd;
        row_template = '<tr><td class="pl-15"><a>'+name+'</a><br><small class="text-info">' + email + '@iqanat.kz</small></td><td class="text-center"><span class="label label-success">Generated Student Preview</span></td><td class="text-center">Today</td><td class="text-center"><span class="label label-success">Yes</span></td></tr>';
        preview += row_template;
    }

    $('#preview-dynamyc-table').find("tr:gt(0)").remove();
    // $('#preview-dynamyc-table').append('<tr><td class="pl-15"><a>Ivan Pupkin</a><br><small class="text-info">email@example.com</small></td><td class="text-center"><span class="label label-success">Generated Student</span></td><td class="text-center">Today</td><td class="text-center"><span class="label label-success">Yes</span></td></tr>');
    $('#preview-dynamyc-table').append(preview);
    // $("#student-list-preview-text").text("");
    // $("#student-list-preview-text").append(text_preview);
}

// SuperCreateStudentsModule.prototype._ajaxSuccess = function(type, pageview, data, status, $xhr) {
//     if (pageview) {
//         ga_report_pageview();
//     }
//     switch (type) {
//         case "cart":
//             this._$xhr = undefined;
//             this._apply(data);
//             this._curtainsUp();
//             break;
//         case "checkout":
//             if (data.success) {
//                 Turbolinks.visit(data.url);
//             } else {
//                 this._$xhr = undefined;
//                 this._curtainsUp();
//                 this._$errorModalBody.text(data.message);
//                 this._$errorModal.modal("show");
//             }
//             break;
//     }
// }
// SuperCreateStudentsModule.prototype._ajaxError = function($xhr, status, error) {
//     this._$failureModal.modal("show");
// }