(function($) {
  'use strict';

    var navSearch = $('.top-icons__search');
    var popupSearch = $('.search-popup');
    var popupSearchClose = $('.search-popup__close');

    var navToggle = $('.nav-toggle__icon');
    var nav = $('.nav');
    var contentOverlay = $('.content-overlay');

    navSearch.on('click', function(){
      popupSearch.addClass('search-popup--active').find('input[type="text"]').focus();
    });

    popupSearchClose.on('click', function(){
      popupSearch.removeClass('search-popup--active');
    });

    navToggle.on('click', function(){
      nav.addClass('nav--mobile');
      contentOverlay.addClass('content-overlay--active');
    });

    contentOverlay.on('click', function(){
      nav.removeClass('nav--mobile');
      contentOverlay.removeClass('content-overlay--active');
    });
  
    $(function(){
		$('.nav__list').slicknav({
        prependTo: '.nav',
		allowParentLinks: true
        });
	});
  
    $('.bxslider').bxSlider({
      adaptiveHeight: true,
      mode: 'fade',
      captions: true,
      pager: false,
      auto: true,
      autoHover: true,
      pause: 4000,
      nextText: '<svg><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#icon-arrow-right"></use></svg>',
	  prevText: '<svg><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#icon-arrow-left"></use></svg>',
      touchEnabled: false
    });
  
    $('.sidebar-slider').bxSlider({
      adaptiveHeight: true,
      mode: 'fade',
      captions: false,
      pager: true,
      controls: false,
      auto: true,
      autoHover: true,
      pause: 4000,
      touchEnabled: false
    });
  
})(jQuery);