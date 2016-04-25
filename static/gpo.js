$(document).ready(function() {
	init_button_area();
});

// Read the avalible gpio pins and initial the buttons accordingly.
// Bind the click event to thees buttons.
function init_button_area() {
	$.ajax({ 
		url: "http://" + window.location.host + "/gpio/read/" 
	}).then(function(data) {
		pins = data.data;
		$(".button-area").removeData();
		for (var pin_num in pins) {
			var pin_value = pins [pin_num];
			var id = "button" + pin_num;
			var ID = "#"+id;
			var h2_elem = "<h2> Pin :" + pin_num + "</h2>";
			var icon_elem = "<div class=icon></div>";
			$(".button-area").append( "<div id="+ id +">" + h2_elem + icon_elem + "</div>" );
			if ( pin_value == "1" ) {
				$( ID ).addClass ( "on" );
			} else {
				$( ID ).addClass ( "off" );
			}
			$( ID ).click ( 
				function(event) { 
					set_gpio(event); 
				} );
			}
	});
}

// When the button been clicked, sending ajax request to change gpio state.
function set_gpio(event){
	var id = event.currentTarget.id ;
	var ID = "#"+id;
	var pin_num = id.replace("button", "");
	// Check if the class is on
	if ( $( ID ).hasClass ("on") ){
		// if current status is on, then turn off
		$.ajax({ url: "http://" + window.location.host + "/gpio/off/" + pin_num + "/" });
	}
	else {
		// else: (current status is off), then turn on
		$.ajax({ url: "http://" + window.location.host + "/gpio/on/" + pin_num + "/" });
	}
	$( ID ).toggleClass( "on" );
	$( ID ).toggleClass( "off" );
}
