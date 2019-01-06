function collapse_x_panel(){
	$('.collapsed')
	.css('height', 'auto')
	.find('.collapse-link i').toggleClass('fa-chevron-up fa-chevron-down').end()
	.find('.x_content').css('display', 'none');
}

$(document).ready(function(){
	collapse_x_panel();
});