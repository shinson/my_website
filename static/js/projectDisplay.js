$(document).ready(function(){
	$('.projectSquare').on("click", function(){
		var el = $(this).children().data('target');
		var selectEl = $('#'+el);
		var parentEl = selectEl.parent();

		

		if(!selectEl.hasClass('isDisplay')){
			$('.projectTable').removeClass('isDisplay');
			selectEl.addClass('isDisplay');
			if(parentEl.is(':hidden')){parentEl.slideDown(500);}
			
		} else {
			selectEl.removeClass('isDisplay');
			parentEl.slideUp(500);
		}
		
	});
});