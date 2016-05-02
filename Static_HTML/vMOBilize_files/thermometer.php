<?php
/***
	----------------------------------------------------------------------------------------------------------------------
	Fundraising Thermometer Class
	----------------------------------------------------------------------------------------------------------------------
	Purpose			: This class handles the generation of a Fundraising Thermometer image. 
	Author			: Nars Mondejar III (narsmondejar@odesk.com)
	----------------------------------------------------------------------------------------------------------------------
	VERSION HISTORY
	v.1.0	2010-06-30	NKM		Initial version
	v.1.1	2010-11-15	NKM		Fix problem on "Goal" and "Raised" texts. Use images instead of dynamic generation.
	v.1.5	2010-11-17	NKM		Added color and size customization parameters.
								Small revamp on the fundraising thermometer image (adjustments to scales).
	----------------------------------------------------------------------------------------------------------------------
***/
class thermometer {
	var $width;
	var $height;
	
	function thermometer () {
	}
	
	function generateThermoImg( $p_currency, $p_goal, $p_current, $p_color, $p_size ) {
		// 1. Initialize currency, font, image dimensions
		switch( $p_currency ) {
			case "dollar": 
			default:		$sign = '&#36;';				// '$'
							$dec_point = '.';
							$thousands_sep = ',';
							break;
			case "euro":	$sign = '&#8364; ';				// '€'
							$dec_point = ',';
							$thousands_sep = ' ';
							break;
			case "pound":	$sign = '&#163; ';				// '£'
							$dec_point = ',';
							$thousands_sep = ' ';
							break;
			case "yen":		$sign = '&#165; ';				// '¥'
							$dec_point = '.';
							$thousands_sep = ',';
							break;
			case "none":	$sign = '';						// no currency
							$dec_point = '.';
							$thousands_sep = ',';
		}
		if( $p_goal > 99999999 ) $p_goal = 99999999;
		if( $p_goal < 0 ) $p_goal = 0;
		if( $p_current > 99999999 ) $p_current = 99999999;
		if( $p_current < 0 ) $p_current = 0;
		switch( $p_color ) {
			case 'red':
			case 'green':
			case 'blue':	break;
			default:		$p_color = 'red';
		}
		switch( $p_size ) {
			case 'medium':
			case 'large':	break;
			default:		$p_size = 'large';
		}
		$img_therm_empty =	dirname(__FILE__) . '/thermo-files/' . $p_size . '/thermo_empty_' . $p_color . '.png';
		$img_therm_scale =	dirname(__FILE__) . '/thermo-files/' . $p_size . '/thermo_scale.png';
		$img_surface =		dirname(__FILE__) . '/thermo-files/' . $p_size . '/surface_' . $p_color . '.png';
		$img_mercury =		dirname(__FILE__) . '/thermo-files/' . $p_size . '/mercury_' . $p_color . '.png';
		$img_pointer =		dirname(__FILE__) . '/thermo-files/pointer_' . $p_color . '.png';
		$img_goal_text =	dirname(__FILE__) . '/thermo-files/text_goal.png';
		$img_raised_text =	dirname(__FILE__) . '/thermo-files/text_raised.png';
		$font_face =		dirname(__FILE__) . '/thermo-files/arial.ttf';
		$font_face_bold =	dirname(__FILE__) . '/thermo-files/arialbd.ttf';
		$font_face_bdit =	dirname(__FILE__) . '/thermo-files/arialbi.ttf';
		$font_size = 10;
		$str_goal = $sign . number_format( $p_goal, 0, $dec_point, $thousands_sep );
		$str_current = $sign . number_format( $p_current, 0, $dec_point, $thousands_sep );
		$box_goal = @imagettfbbox( $font_size, 0, $font_face, $str_goal );
		$box_curr = @imagettfbbox( $font_size, 0, $font_face, $str_current );
		$scale_width = abs( $box_goal[0] ) + abs( $box_goal[2] );	// + 7;
		$raised_width = abs( $box_curr[0] ) + abs( $box_curr[2] );	// + 5;
		
		$padding_left = 20;
		$padding_top = 30;
		$percent_scale_height = ( $p_size == 'large' ) ? 330 : 225;
		$mercury_left = ( $p_size == 'large' ) ? 20 : 13;
		$mercury_base = ( $p_size == 'large' ) ? 347 : 233;
		$mercury_width = ( $p_size == 'large' ) ? 21 : 15;
		$mercury_height = ( $p_size == 'large' ) ? 21 : 15;
		$meniscus_top = ( $p_size == 'large' ) ? 345 : 232;
		$meniscus_width = ( $p_size == 'large' ) ? 21 : 15;
		$meniscus_height = ( $p_size == 'large' ) ? 5 : 4;
		$thermo_center = ( $p_size == 'large' ) ? 30 : 21;
		$thermo_width = ( $p_size == 'large' ) ? 55 : 37;
		$thermo_height = ( $p_size == 'large' ) ? 400 : 270;
		$scale_txt_top = 3;
		$scale_txt_width = 30;
		$scale_txt_height = 12;
		$goal_base = 28;
		$scale_left = ( $p_size == 'large' ) ? 25 : 17;
		$scale_top = ( $p_size == 'large' ) ? 15 : 8;
		$scale_img_width = ( $p_size == 'large' ) ? 16 : 11;
		$scale_img_height = ( $p_size == 'large' ) ? 335 : 227;
		$zero_scale_left = ( $p_size == 'large' ) ? -5 : -8;
		$zero_scale_base = ( $p_size == 'large' ) ? 353 : 238;
		$pointer_left = ( $p_size == 'large' ) ? 45 : 32;
		$pointer_top = ( $p_size == 'large' ) ? 335 : 222;
		$pointer_width = 30;
		$pointer_img_width = 26;
		$pointer_img_height = 26;
		$current_base = ( $p_size == 'large' ) ? 345 : 232;
		$raised_txt_top = ( $p_size == 'large' ) ? 350 : 237;
		$raised_txt_width = 45;
		$raised_txt_height = 11;
		
		$this->width = $padding_left + $thermo_width + $pointer_img_width + max( $raised_width, $raised_txt_width );
		$this->height = ( $p_size == 'large' ) ? 430 : 300;
		
		// 2. Load the PNG stock images and allocate memory for our color identifiers
		//    Should any of the memory allocations fail, we must return immediately and return an error image
		if( FALSE === ( $im_src_empty = @imagecreatefrompng( $img_therm_empty ))) return FALSE;
		if( FALSE === ( $im_src_scale = @imagecreatefrompng( $img_therm_scale ))) return FALSE;
		if( FALSE === ( $im_src_surf = @imagecreatefrompng( $img_surface ))) return FALSE;
		if( FALSE === ( $im_src_merc = @imagecreatefrompng( $img_mercury ))) return FALSE;
		if( FALSE === ( $im_src_ptr = @imagecreatefrompng( $img_pointer ))) return FALSE;
		if( FALSE === ( $im_src_goal = @imagecreatefrompng( $img_goal_text ))) return FALSE;
		if( FALSE === ( $im_src_raised = @imagecreatefrompng( $img_raised_text ))) return FALSE;
		if( FALSE === ( $im_dest = @imagecreatetruecolor( $this->width, $this->height ))) return FALSE;
		if( FALSE === ( $transparent = @imagecolorallocatealpha($im_dest, 0, 0, 0, 127))) return FALSE;
		if( FALSE === ( $txt_color_black = @imagecolorallocate( $im_dest, 0, 0, 0 ))) return FALSE;
		if( FALSE === ( $txt_color_gray = @imagecolorallocate( $im_dest, 109, 110, 113 ))) return FALSE;
		if( FALSE === ( $txt_color_red = @imagecolorallocate( $im_dest, 238, 62, 52 ))) return FALSE;

		// 3. Fill destination image with white background and overlay the empty thermometer image
		@imagesavealpha( $im_dest, true );
		@imagefill( $im_dest, 0, 0, $transparent );
		@imagecopy( $im_dest, $im_src_empty, $padding_left, $padding_top, 0, 0, $thermo_width, $thermo_height );

		// 4. Draw the mercury, scaling depending on the percentage
		if( $p_goal > 0.0 )
			$percent = $p_current / $p_goal;
		else
			$percent = $p_current / 0.00001;
		if( $percent > 1.0 ) $percent = 1.0;
		@imagecopyresampled( $im_dest, $im_src_merc, $padding_left+$mercury_left, $padding_top+$mercury_base-floor( $percent_scale_height*$percent ), 0, 0, $mercury_width, 2+round( $percent_scale_height*$percent ), $mercury_width, $mercury_height );

		// 5. Draw the mercury surface (meniscus)
		@imagecopy( $im_dest, $im_src_surf, $padding_left+$mercury_left, $padding_top+$meniscus_top-($percent_scale_height*$percent), 0, 0, $meniscus_width, $meniscus_height );

		// 6. Add the goal scale text
		@imagecopy( $im_dest, $im_src_goal, $padding_left+$thermo_center-floor( $scale_txt_width/2 ), $scale_txt_top, 0, 0, $scale_txt_width, $scale_txt_height );
		@imagettftext( $im_dest, $font_size, 0, $padding_left+$thermo_center-floor( $scale_width/2 ), $goal_base, $txt_color_black, $font_face, $str_goal );
		@imagettftext( $im_dest, $font_size, 0, $padding_left+$zero_scale_left, $padding_top+$zero_scale_base, $txt_color_black, $font_face, $sign . '0' );
		@imagecopy( $im_dest, $im_src_scale, $padding_left+$scale_left, $padding_top+$scale_top, 0, 0, $scale_img_width, $scale_img_height );
		
		// 7. Add arrow pointer & raised amount text
		@imagecopy( $im_dest, $im_src_ptr, $padding_left+$pointer_left, $padding_top+$pointer_top-($percent_scale_height*$percent), 0, 0, $pointer_img_width, $pointer_img_height );
		@imagecopy( $im_dest, $im_src_raised, $padding_left+$pointer_left+$pointer_width, $padding_top+$raised_txt_top-($percent_scale_height*$percent), 0, 0, $raised_txt_width, $raised_txt_height );
		if( $p_current < $p_goal )
			@imagettftext( $im_dest, $font_size, 0, $padding_left+$pointer_left+$pointer_width, $padding_top+$current_base-($percent_scale_height*$percent), $txt_color_black, $font_face, $str_current );
		else {
			// 2010-07-02:	Separate exclamation point and make it italicized and 2pts larger than the amount's font size
			@imagettftext( $im_dest, $font_size, 0, $padding_left+$pointer_left+$pointer_width, $padding_top+$current_base-($percent_scale_height*$percent), $txt_color_red, $font_face_bold, $str_current );
			@imagettftext( $im_dest, $font_size+2, 0, $padding_left+$pointer_left+$pointer_width+$raised_width, $padding_top+$current_base-($percent_scale_height*$percent), $txt_color_red, $font_face_bdit, '!' );
		}

		// 8. Output the generated image to the browser
		header( 'Content-type: image/png' );
		@imagepng( $im_dest );

		// 9. Lastly, free the allocated memory of our images & color resources
		@imagecolordeallocate( $txt_color_red );
		@imagecolordeallocate( $txt_color_gray );
		@imagecolordeallocate( $txt_color_black );
		@imagecolordeallocate( $transparent );
		@imagedestroy( $im_dest );
		@imagedestroy( $im_src_raised );
		@imagedestroy( $im_src_goal );
		@imagedestroy( $im_src_ptr );
		@imagedestroy( $im_src_merc );
		@imagedestroy( $im_src_surf );
		@imagedestroy( $im_src_scale );
		@imagedestroy( $im_src_empty );

		return TRUE;
	}
}

/***
	----------------------------------------------------------------------------------------------------------------------
	Start of main code
	----------------------------------------------------------------------------------------------------------------------
***/

// Protect PHP Globals
$vars = array( '$_GET', '$_POST', '$_FILES', '$_SERVER', '$_SESSION', '$_COOKIE' );		// Each global array to sort.
foreach( $vars as $var ) {
	if( is_array( $var )) {
		foreach ($var as $key => $value) {
			$key = strip_tags( $key );													// Remove any tags from the key
			$value = strip_tags( $value );												// Remove any tags from the value
			$var[$key] = htmlentities( $value, ENT_QUOTES ); 							// Convert all applicable characters to HTML entities
		}
	}
}

// Ensure we have the correct parameters, otherwise, set default values
if( FALSE === isset( $_GET['currency'] )) $_GET['currency'] = 'dollar';
if( FALSE === isset( $_GET['goal'] )) $_GET['goal'] = 0;
if( FALSE === isset( $_GET['current'] )) $_GET['current'] = 0;
if( FALSE === isset( $_GET['color'] )) $_GET['color'] = 'red';
if( FALSE === isset( $_GET['size'] )) $_GET['size'] = 'large';

// Now we generate our image
$therm = new thermometer();
if( FALSE === $therm->generateThermoImg( strtolower( $_GET['currency'] ), intval( $_GET['goal'] ), intval( $_GET['current'] ), strtolower( $_GET['color'] ), strtolower( $_GET['size'] ))) {
	//die( 'PHP GD ERROR: Cannot initialize new GD image stream. Thermometer image could not be generated.' );
	header( 'Content-type: image/png' );
	$f = fopen( dirname(__FILE__) . '/thermo-files/gd_error.png', 'r' );
	while( !feof( $f ))
		echo fread( $f, 8192 );
	fclose( $f );
}
?>