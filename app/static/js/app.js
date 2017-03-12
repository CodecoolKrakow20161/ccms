$(document).ready(function() {
    $("a.submit-form").click(function() {
        form_id = $(this).data('form-id')
        answer = confirm("Are you sure you want to remove this record?")
        if (form_id != "Undefined" && answer) {
            $("#" + form_id).submit()
        }
    });
});