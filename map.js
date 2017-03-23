/* map.js - display map and update position as reported by web service */

var interval = 1000;

// GUI objects
var map, infowindow, drawingManager;
var contentString = '<span id="msg"></span><br id="msg"/><span id="lat">?</span>, <span id="lng">?</span><br/>\
<span id="speed">?</span> mph, <span id="course">?</span>&deg<br/>\
Last Updated: <span id="last">?</span>';
var currentIcon = 'jeep-icon.png';
var trailIcon = 'circle.png';

// Model
var speed, course, message;
var marker = [];

function update() {
	message = "";
	course = "0";
	speed = "0";
	$.getJSON("status.py", function(resp) {
		r = resp[0];
		console.log(r);	
		// TODO: modify for extended format parameters
		var lat = parseFloat(r.lat).toFixed(6);
		var lng = parseFloat(r.lng).toFixed(6);
		var position = new google.maps.LatLng(lat, lng);
		// update infowindow
		$("span#lat").text(lat);
		$("span#lng").text(lng);
		$("span#speed").text(r.speed);
		$("span#course").text(r.course);
		$("span#msg").text(r.msg);
		if (r.msg != "") {
			$("br#msg").show();
		} else {
			$("br#msg").hide();
		}
		$("span#last").text(r.time);
  	infowindow.open(map, marker[0]);
		// Shift markers
		// Set position of marker 0 (current position)
		marker[0].setPosition(position);
		map.panTo(position);
	});
} // update

function initMap() {
	map = new google.maps.Map(document.getElementById('map'));
	infowindow = new google.maps.InfoWindow({
		content: contentString
	});
	$.getJSON("status.py?history=10", function(resp) {
		for (e of resp) {
			console.log(e);
			lat = parseFloat(e.lat).toFixed(6);
			lng = parseFloat(e.lng).toFixed(6);
			position = new google.maps.LatLng(lat, lng);
			marker.push(new google.maps.Marker({
				position: position,
				map: map,
				icon: trailIcon
			}));
		}
		map.setZoom(12);
		map.panTo(position);	
		marker[0].setIcon(currentIcon);
	});
	setInterval(update, interval);
}

$(window).resize(function() {
	update();
});

$("form").submit(function() {
});


