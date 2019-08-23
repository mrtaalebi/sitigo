$(document).scroll(function() {
  if ($(this).scrollTop() > $(window).height()) {
    $('.register-scroll').css('display', 'flex');
  } else {
    $('.register-scroll').css('display', 'none');
  }
});
