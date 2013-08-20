function initialize () {
	var mapOptions = {
		zoom: 11,
		center: new google.maps.LatLng(-33.5237864105204, -70.78244524999997),
		disableDefaultUI: true,
		zoomControl: false,
		scaleControl: false,
		scrollwheel: false,
		disableDoubleClickZoom: true,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	}
 
	var map = new google.maps.Map(document.getElementById('mapa'), mapOptions);

    var icono = new google.maps.Marker({
     	   	position: new google.maps.LatLng(-33.5237864105204, -70.78244524999997),
        	icon: 'http://themadrid.cl/static/media/img/map_marker.png',
        	map: map               
    });
}

function changeClass(id){
	jQuery('.current').attr('class', '');
	jQuery('#'+ id).parent().attr('class', 'current');
}


jQuery(document).on('ready',function(){
	jQuery('body').delegate('#btnContact', 'click',function(){
		jQuery('#contactForm').submit(function(){
			var data = jQuery('#contactForm').serialize();

			jQuery.ajax({
				url : '/contact',
				type: 'post',
				data: data,
				dataType: 'json',
				success: function(data){
					jQuery('.errorlist').remove();
					if(data.ok === 'not'){
						var input = $('#contactForm input');
						jQuery.each(data.errors,function(index,val){
							jQuery(input).each(function(indice, value){
								var name = jQuery(this).attr('name');
								if(name === index){
									jQuery(this).before("<span class='errorlist'>"+ val + "</span>");
								}
							});
								
						});
						
						initialize();
					}else{
						jQuery('.errorlist').remove();
						jQuery('input[type=text]').val('');
							jQuery('input[type=tel]').val('');
							jQuery('input[type=email]').val('');
							jQuery('textarea').val('');
							jQuery.fancybox(
								'<p>Mensaje enviado exitosamente, gracias por el contacto.</p><br /><p> Me comunicare con Ud. según corresponda.</p>',
								{
									'width' : 350,
									'height': 100
								}
							);
					}
					
				},
				complete: function(){

				}
			});
			return false;
		});
	});
});