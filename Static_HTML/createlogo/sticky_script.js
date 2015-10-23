/*
*  Homework Problem #2
*  sticky_script.js
*  CS171
*  Submitted by: James Curtin
*/

var number = 0;

function addSticky (form) {
	$("#list ul").append("<div><li><a><img id='myimage' src='" + form.logo.value + "'><h2>" + form.title.value + "</h2></a></li><div>");
	$("#delete select").append("<option value='" + (number - 1) + "'>" + number + "</option>");
};