
$(document).ready(function(){
	$("#btn-menu").on("click", function(){
		var menu = $(this).children();
		$(this).find("button").toggleClass("is-active");
		
		$(this).find('#menuList').toggleClass("showMenu");
		
	});

	$('#menuList').find('li').on("click", function(){
	    var $href = $(this).data("target");
	    if($href==="media"||$href==="project"){
			var test = $('.mediaProjects').css('display');
			$href = test === 'flex' ? 'mediaProjects': $href;
		}
		
		var $anchor = $('#'+$href).offset();
		
		console.log($href);
	    $('body').animate({ scrollTop: $anchor.top });
	});
});
