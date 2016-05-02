/**
 * Created by jamescurtin on 3/3/16.
 */

console.log("test");

//$(".badge").each(function() {repeat(this)});

function repeat(item) {
    $("#images").animate({
        left: '50px',
        height: '45px',
        width: '50px'
    }, "slow");
    $("#images").animate({
        left: '0px',
        width:'34px',
        height: '37px',
    }, "slow");
}

//$("#stars").animate({
//    width: '178px',
//    height: '215px',
//}, "slow");
////$("#images").animate({
////    width:'125%',
////    height: '125%',
////}, "slow");
//$("#stars").animate({
//    width:'142px',
//    height: '171px',
//}, "slow");
//$("#images").animate({
//    width:'100%',
//    height: '100%',
//}, "slow");


var backgroundInterval = setInterval(function(){
    $(".newbadge").toggleClass("backgroundGold");
},500);
backgroundInterval();