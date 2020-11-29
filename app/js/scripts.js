$(document).ready(function () {

	// Banner - Carousel
	$('.blog__slaider').owlCarousel({
		items: 3,
		loop: true,
		nav: false,
		dots: true,
		margin: 30,
		responsive : {
			0 : {
				items: 1
			},
			480 : {
				items: 2
			},
			768 : {
				items: 3
			}
		}
	});

	$('.logo__bars').click(function(){
		$('.navigation').slideToggle(500);
	})

});