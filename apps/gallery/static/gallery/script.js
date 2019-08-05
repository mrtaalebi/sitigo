$(document).ready(function () {
    $(".open-modal").click(function(){
	    $('.modal').fadeIn();
        $('.modal-image').attr("src", $(this).attr("src"));
        $('.modal-image').attr("alt", $(this).attr("alt"));
        $('.modal-caption').html($(this).attr("alt"))
	});
	$('.modal').click(function(){
        $('.modal-image').attr("src", "");
        $('.modal-image').attr("alt", "");
        $('.modal-caption').html("");
		$('.modal').fadeOut();
	});

    $(".show-caption").hover(
        function() {
            var select = "#caption_" + $(this).attr("id");
            $(select).fadeIn();
        },

        function() {
            var select = "#caption_" + $(this).attr("id");
            $(select).fadeOut();
        }
    );
});
