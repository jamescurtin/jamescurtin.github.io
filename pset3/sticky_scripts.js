/*
*  Homework Problem #3
*  sticky_scripts.js
*  CS171
*  Submitted by: James Curtin
*/

// Sets a counter used to number future sticky notes
var number = 0;

// Functionality for adding a sticky note to the page
function addSticky (form) {
	$("#list ul").append("<li><a href='" + form.link.value + "' target='_blank'><h2>" + 
		form.title.value + " (#" + (number + 1) + ")</h2><p>" + form.content.value + "</p></a></li>");
	number = ++number;
	$("#delete select").append("<option value='" + (number - 1) + "'>" + number + "</option>");
};

// Functionality for deleting a sticky note from the page
function deleteSticky (form) {
	var list = document.getElementById("stickies");
    list.removeChild(list.childNodes[form.number.value]);
};

// Accesses the users geolocation
function getGeo () {
	var x = document.getElementById("demo");
	function getLocation() {
	    if (navigator.geolocation) {
	        navigator.geolocation.getCurrentPosition(showPosition);
	    } else {
	        x.innerHTML = "Geolocation is not supported by this browser.";
	    }
	}
	function showPosition(position) {
	    x.innerHTML = "Latitude: " + position.coords.latitude + 
	    "<br>Longitude: " + position.coords.longitude; 
	}
};