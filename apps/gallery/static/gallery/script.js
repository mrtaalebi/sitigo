$(function () {
    "use strict";
    
    $("document.querySelector('#topper > div > div.ui.stackable.grid > div.twelve.wide.center.aligned.stretched.column > div > div > div > div > div > img')").click(function () {
        var $src = $(this).attr("src");
        $("#topper > div > div.ui.stackable.grid > div.twelve.wide.center.aligned.stretched.column > div > div.show").fadeIn();
        $(".img-show img").attr("src", $src);
    });
    
    $(".overlay").click(function () {
        $(".show").fadeOut();
    });
    
});
