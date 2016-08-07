            window.onload = function() {
                if (screen.width <= 800) {
                    $( ".icon-circle" ).remove();
                    $( ".pg-icon lightbox-icon" ).remove();
                    $( ".qg-title" ).remove();
                    $( "div.slider" ).remove();
                    $( "a" ).removeAttr("data-rel");
                    $('.quick-gallery a').contents().unwrap();
                    $( ".qg-full-col-3" ).addClass('qg-full-col-1').removeClass('qg-full-col-3');
                }
            }