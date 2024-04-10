// Show the proper div on radio button click
$(document).delegate(".panel-understanding-check .radio input", "click", function() {

    // Create the ID for the answer div from the question number
    var dataQuestionNumber = "#" + $(this).data("question-number");
  
    // Show the comment div
    $(dataQuestionNumber).removeClass("hidden");
  
    // Get the comment and alert type data attributes
    var alertContent = $(this).data("comment");
    var alertType = $(this).data("alert-type");
  
    // Write the comment and alert type to the div
    $(dataQuestionNumber).html(alertContent);
    $(dataQuestionNumber).removeClass("alert-danger").removeClass("alert-warning").removeClass("alert-success").addClass(alertType);
  });