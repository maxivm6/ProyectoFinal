$(document).on('mousewheel', function(event) {

    alert("hola");

    event.preventDefault();
    var scrolled = $(window).scrollTop();
    $(window).scrollTop(scrolled - event.deltaY);
  });