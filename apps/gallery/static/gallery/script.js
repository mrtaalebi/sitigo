$(window).load(function () {
    $(".o-my-sweet-image").click(function () {
        var $src = $(this).attr("src");
        $(".show").fadeIn();
        $(".img-show img").attr("src", $src);
    });
    
    $(".overlay").click(function () {
        $(".show").fadeOut();
    });
    
});
