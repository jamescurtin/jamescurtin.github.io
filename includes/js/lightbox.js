/*
Theme Name: Story
Distributed by Pexto Themes
License: GNU General Public License v2 or later
License URI: http://www.gnu.org/licenses/gpl-2.0.html
*/

var SITE = SITE || {};
SITE.lightboxOptions = {
	"theme":"pp_default","animation_speed":"normal","overlay_gallery":false,"allow_resize":true};
	SITE.disableRightClick=true;
	SITE.stickyHeader=true;
	jQuery(document).ready(function($){
					SITE.init.initSite();
					new SITE.Fullpage(".section", {"animateElements":true,"autoplay":true,
						"autoplayInterval":4000,"horizontalAutoplay":true}).init();
				});