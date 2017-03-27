/* map.js - display map and update position as reported by web service */

var interval = 5000;

// View objects
var map, infowindow, drawingManager;
var contentString = '<span id="msg"></span><br id="msg"/><span id="lat">?</span>, <span id="lng">?</span><br/>\
<span id="speed">?</span> mph, <span id="course">?</span>&deg<br/>\
Last Updated: <span id="last">?</span>';
var currentIcon = 'jeep-icon.png';
var trailIcon = 'circle.png';

// TODO: modify for extended format parameters

var maxLength = 30

// Model
// Status: lat, long, course, speed, marker, infowindow
var report = [];
var lastTime = 0; // timestamp of most recent report
// Message:
var message = [];

///////////////////////////////////////////////////////////////////////
// Inserts a new report object if id is new
function addReport(time, lat, lng, course, speed, text) {	
	mytime = Date.parse(time);
	if (mytime <= lastTime)
		return;
	// change icon
	if (report.length > 0)
		report[report.length-1].marker.setIcon(trailIcon);
	var newReport = {
		'time': mytime,
		'lat': parseFloat(lat).toFixed(6),
		'lng': parseFloat(lng).toFixed(6),
		'course': parseInt(course),
		'speed': parseInt(speed),
		'text': text
	}
	console.log(newReport);
	newReport.marker = new google.maps.Marker({
				position: new google.maps.LatLng(newReport.lat, newReport.lng),
				map: map,
				icon: currentIcon
	});
	report[report.length] = newReport;
	map.panTo(newReport.marker.position);
	lastTime = newReport.time;
}


///////////////////////////////////////////////////////////////////////
// 
function updateInfoWindow() {
	$("span#lat").text(lat);
	$("span#lng").text(lng);
	$("span#speed").text(r.speed);
	$("span#course").text(r.course);
	$("span#msg").text(r.text);
	if (r.msg != "") {
		$("br#msg").show();
	} else {
		$("br#msg").hide();
	}
	$("span#last").text(r.time);
}

///////////////////////////////////////////////////////////////////////
// polls for most recent status
function pollForUpdate() {
	$.getJSON("status.py", function(resp) {
		s = resp[0];
		console.log(s);
		addReport(s.time, s.lat, s.lng, s.course, s.speed);
	});
}

///////////////////////////////////////////////////////////////////////
// Initializes map application
function initMap() {
	map = new google.maps.Map(document.getElementById('map'));
  map.setZoom(14);
  map.panTo({'lng': -104.932838, 'lat': 39.597550});
	infowindow = new google.maps.InfoWindow({
		content: contentString
	});
	$.getJSON("status.py?history="+maxLength, function(resp) {
		for (s of resp) {
			console.log(s)
			addReport(s.time, s.lat, s.lng, s.course, s.speed, s.text);
		}
		setInterval(pollForUpdate, interval);
	});
}

$(window).resize(function() {
	update();
});

$("form").submit(function() {
});


