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