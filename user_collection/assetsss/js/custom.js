/** Navbar **/

(function($) {
    "use strict"; // Start of use strict

    // jQuery for page scrolling feature - requires jQuery Easing plugin
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: ($($anchor.attr('href')).offset().top - 50)
        }, 1250, 'easeInOutExpo');
        event.preventDefault();
    });

    // Highlight the top nav as scrolling occurs
    $('body').scrollspy({
        target: '.navbar-fixed-top',
        offset: 100
    });

    // Closes the Responsive Menu on Menu Item Click
    $('.navbar-collapse ul li a').click(function() {
        $('.navbar-toggle:visible').click();
    });

    // Offset for Main Navigation
    $('#mainNav').affix({
        offset: {
            top: 50
        }
    })

})(jQuery); // End of use strict


/** Preloader **/

$(window).load(function() { // makes sure the whole site is loaded
   var preloader=$('#preloader div');
   preloader.fadeOut(); // will first fade out the loading animation
   $('#preloader').delay(350).fadeOut('slow'); 
// will fade out the white DIV that covers the website.
      $('body').delay(350).css({'overflow':'visible'});
}) 


jQuery(document).ready(function($) {


    // Counter
    $('.counter').counterUp({
        delay: 10,
        time: 1000
    });

    //Top Slider
    $('#top-slider').bsTouchSlider();

    // Agents
    $('#media').carousel({
      pause: true,
      interval: false,
    });

});


