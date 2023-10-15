$(document).ready(function() {

var x = false;

$('#inf h3').click(function(){

	if(x == false){
		$(this).next().slideDown();
		$(this).addClass('close');
		x = true;
	} else {
		$(this).next().slideUp();
		$(this).removeClass('close');
		x = false;
	}
});





var y = false;

$('.zap, .tr').click(function(){

	if(y == false){
		$('.infa').fadeIn();
		y = true;
	} else {
		$('.infa').fadeOut();
		y = false;
	}
});



var z = false;

$('.zapa, .tra').click(function(){

	if(z == false){
		$('.infaa').fadeIn();
		z = true;
	} else {
		$('.infaa').fadeOut();
		z = false;
	}
});

});