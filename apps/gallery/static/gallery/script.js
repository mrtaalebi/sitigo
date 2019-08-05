$(function () {
    "use strict";
    
    var images = document.querySelectorAll('.o-my-sweet-image')
    
    images.click(function () {
        var $src = $(this).attr("src");
        $(".show").fadeIn();
        $(".img-show img").attr("src", $src);
    });
    
    $(".overlay").click(function () {
        $(".show").fadeOut();
    });
    
});
