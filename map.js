/* map.js - display map and update position as reported by web service */

var interval = 1000;
var position;
var speed, course, message;
var map, marker, infowindow, drawingManager;
var contentString = '<span id="msg"></span><br id="msg"/><span id="lat">?</span>, <span id="lng">?</span><br/>\
<span id="speed">?</span> mph, <span id="course">?</span>&deg<br/>\
Last Updated: <span id="last">?</span>';

function update() {
	message = "";
	course = "0";
	speed = "0";
	$.getJSON("status.py", function(r) {
		console.log(r);
		// TODO: modify for extended format parameters
		lat = parseFloat(r[0].lat).toFixed(6);
		lng = parseFloat(r[0].lng).toFixed(6);
		position = new google.maps.LatLng(lat, lng);
		speed = r[0].speed;
		course = r[0].course;
		msg = r[0].msg;
		last = r[0].time;
		$("span#lat").text(lat);
		$("span#lng").text(lng);
		$("span#speed").text(speed);
		$("span#course").text(course);
		$("span#msg").text(msg);
		if (msg != "") {
			$("br#msg").show();
		} else {
			$("br#msg").hide();
		}
		$("span#last").text(last);
  	infowindow.open(map, marker);	
		marker.setPosition(position);
		map.panTo(position);
		
		// Display previous locations
		for (i=1; i < r.length && i < 50; i++) {
			var m = new google.maps.Marker({
				position: new google.maps.LatLng(r[i].lat, r[i].lng),
				map: map,
				icon: 'circle.png'
			});
		}
	});
	window.setTimeout(update, interval);
	interval = 10000;
}

function initMap() {
	map = new google.maps.Map(document.getElementById('map'), {
		zoom: 12,
		center: position
	});
	marker = new google.maps.Marker({
		position: position,
		map: map,
		icon: 'jeep-icon.png'
	});
	infowindow = new google.maps.InfoWindow({
		content: contentString
	});
	update();
}

$(window).resize(function() {
	update();
});

$("form").submit(function() {
});


