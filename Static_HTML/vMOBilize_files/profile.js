$(function() {
  $(".unearned-badge img").hover(function() {
    $(this).attr("src",$(this).attr("earned"));
  }, function() {
    $(this).attr("src",$(this).attr("unearned"));    
  });
  
  $(".badge").click(function() {
    $("#badge_modal .modal-title").html($(this).attr("name"));
    $("#badge_modal .modal-body").html($(this).attr("description"));
    $("#badge_modal").modal('show');
  });
});