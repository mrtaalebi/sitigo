$(document).ready(function () {

    function set_image(img) {
        $('.modal-image').attr("src", $(img).attr("src"));
        $('.modal-image').attr("alt", $(img).attr("alt"));
        $('.modal-caption').html($(img).attr("alt"));
    }

    $('.open-modal').click(function() {
        $('.modal').fadeIn();
        set_image(this);
	});

	$('.close-modal').click(function() {
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


    var images = $(".slide");
    $(".prev-slide").click(function() {
        for (var i = 0; i < images.length; i++) {
            if ($(images[i]).attr("src") == $('.modal-images').attr("src")) {
                set_image(images[ (i - 1) % images.length ]);
                break;
            }
        }
    });
    
    $(".next-slide").click(function() {
        for (var i = 0; i < images.length; i++) {
            if ($(images[i]).attr("src") == $('.modal-images').attr("src")) {
                set_image(images[ (i + 1) % images.length ]);
                break;
            }
        }
    });

});
