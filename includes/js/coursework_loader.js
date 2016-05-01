            window.onload = function() {
                if (screen.width <= 800) {
                    $( "#courseContainer" ).load( "m.coursework.html");
                }
                else{
                    $( "#courseContainer" ).load( "coursework.html");
                }
            }