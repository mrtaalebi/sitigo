$(document).ready(function () {
    $(".open-modal").click(function(){
	    $('.modal').fadeIn();
        $('.modal-image').attr("src", $(this).attr("src"));
        $('.modal-image').attr("alt", $(this).attr("alt"));
        $('.modal-caption').html($(this).attr("alt"))
	});
	$('.modal').click(function(){
		$('.modal').fadeOut();
	});
});
