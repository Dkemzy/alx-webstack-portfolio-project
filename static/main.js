// This code is not necessary for the page to work, but it adds some additional functionality.

window.onload = function() {
  // When the page loads, hide the menu drop down.
  document.getElementById("menu").style.display = "none";

  // When the user clicks on the logo, show the menu drop down.
  document.getElementById("logo").onclick = function() {
    document.getElementById("menu").style.display = "block";
  };

  // When the user clicks outside of the menu drop down, hide it.
  document.addEventListener("click", function(event) {
    if (event.target === document.getElementById("menu")) {
      document.getElementById("menu").style.display = "none";
    }
  });
};
$(window).scroll(function() {
	var $centerImg = $('#center > img')
    , hT = $centerImg.offset().top
    , hH = $centerImg.outerHeight()
    , wH = $(window).height()
    , dH = $(document).height()
    , wS = $(this).scrollTop();
  
  if (wS > (hT+hH-wH)){
    $centerImg.addClass("parallaxin");
  } else {
    $centerImg.removeClass("parallaxin");
    $centerImg.css({
     'transform': 'translate(0,0)'
    });
  }
  
  $('#hero-text').css({
    'transform': 'translate(0, '+ -wS * 0.5 +'px)'
	});
  
  $('.parallaxin').css({
    'transform': 'translate(0, -'+ (wS + 1000 - dH)/4 +'%)'
	});
});

