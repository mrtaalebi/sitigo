$(document).ready(function () {
    $(".trigger_popup_fricc").click(function(){
	    $('.hover_bkgr_fricc').show();
        $('.hover_img_fricc').attr("src", $(this).attr("src"))
	});
	$('.hover_bkgr_fricc').click(function(){
		$('.hover_bkgr_fricc').hide();
	});
	$('.popupCloseButton').click(function(){
		$('.hover_bkgr_fricc').hide();
	});
});
