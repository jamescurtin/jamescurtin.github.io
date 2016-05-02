var periodicRefreshTimer = null;
var lastViewedPoints = 0;
var lastViewedTeamPoints = 0;

$(function() {
  lastViewedPoints = parseInt($('#player_points').html());
  lastViewedTeamPoints = parseInt($('#team_points').html());
  
  $('#popup_invitation').click(function() {
    $('#invitation_popup').toggle();
    $('#invitation_popup input').select();
  });
  
  $('#postnewsbtn').click(postNews);
  try {
    Visibility.every(5000, teamRefresh);
  } catch (ex) { // IE<=9 sucks, just always ping for them
    setInterval(5000, function() {
      teamRefresh();
    }); 
  }
  teamRefresh();
})

function postNews() {
  var jqxhr = $.ajax({
    url: '/news/', 
    type: 'POST',
    dataType: "json",
    data: {
      'message' : $("#postnewstxt").val()
    }
  });
  
  jqxhr.success(function(data, textStatus, jqXHR) {
    if (data['success']) {
      $("#postnewstxt").val(""); // clear the textfield
    }
  });
}

function teamRefresh() {
  // TODO: make sure the page is active
  pingNews();
}

/**
 * Gets the new news items, also updates points (because it's efficient to do so)
 */
function pingNews() {
  var jqxhr = $.ajax({
    url: '/news/', 
    type: 'GET',
    dataType: 'json',
    data : {
      'team_id' : team_id
    }
  });

  jqxhr.success(function(data, textStatus, jqXHR) {
    if (is_my_team) {
      updatePlayerPoints(data['player_points']);
      updateTeamPoints(data['team_points']);      
    }

    $("#newsitems").html("");
    var newsItems = data['items'];
    for (var idx in newsItems) {
      newsItem = newsItems[idx];
      $("#newsitems").append('<div class="newsItem"><img class="newsHeadshot" src="'+newsItem['icon']+'" /><span class="newsUname">'+newsItem['uname']+'</span><span class="newsDate"> -- '+newsItem['dt']+'</span><div class="newsMsg">'+newsItem['m']+'</div></div>');
    }
  });
}

function updatePlayerPoints(player_points) {
  console.log("updatePlayerPoints("+player_points+"):"+lastViewedPoints);
  if (player_points == lastViewedPoints) return;
  var oldVal = lastViewedPoints;
  lastViewedPoints = player_points;
  updatePoints("#player_points", oldVal, lastViewedPoints);
}

function updateTeamPoints(team_points) {
  if (team_points == lastViewedTeamPoints) return;
  var oldVal = lastViewedTeamPoints;
  lastViewedTeamPoints = team_points;
  updatePoints("#team_points", oldVal, lastViewedTeamPoints);
}

function updatePoints(id, oldVal, newVal) {
  console.log("updatePoints("+id+","+oldVal+","+newVal+")");
  $(id).prop('Counter',oldVal).animate({
    Counter: newVal
  }, {
    duration: 1500,
    easing: 'swing',
    step: function (now) {
        $(this).text(Math.ceil(now));
    }
  });
}
