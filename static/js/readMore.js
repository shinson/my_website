$(document).ready(function(){
	$('.icn-more').on("click", function(){
		$(this).parent().next().slideToggle(500);
		$(this).parent().next().toggleClass('isOpen');
	});
});