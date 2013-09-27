
	
	$(window).scroll(function(){
        if ($(this).scrollTop() > 110) {
            $('.top').fadeIn();
        } else {
            $('.top').fadeOut();
        }
    });

	$(document).ready(function() {
		$('.top').click(function() {
			$('html, body').animate({ scrollTop: 0 }, 'medium');
		});
	});
	

