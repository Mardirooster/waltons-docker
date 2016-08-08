
$(document).ready(function(){/* activate sidebar */


/* activate scrollspy menu */
var $body   = $(document.body);
var navHeight = $('.navbar').outerHeight(true) + 10;


$('#sidebar').affix({
  offset: {
    top: navHeight
  }
});

$body.scrollspy({
	target: '#leftCol',
	offset: navHeight
});
console.log(navHeight);
/* smooth scrolling sections */
$('a[href*=#]:not([href=#])').click(function() {
    console.log(navHeight);
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html,body').animate({
          scrollTop: target.offset().top - 50
        }, 10);
        return false;
      }
    }
});
});