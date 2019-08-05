$(document).ready(function () {
    $(".open-modal").click(function(){
	    $('.modal').show();
        $('.modal-image').attr("src", $(this).attr("src"));
        $('.modal-image').attr("alt", $(this).attr("alt"));
        $('.modal-caption').html($(this).attr("alt"))
	});
	$('.open-modal').click(function(){
		$('.modal').hide();
	});
});
