import Config from '../../config.py'

let config = new Config();

function searchLatLong() {
  let lat = $('lat').val();
  let long = $('long').val();

  console.log(lat);
  console.log(long);
}

// check to see if the submit button is pressed, if it is, stop the even from refreshing the page, and call searchAddress()
$('submit_LatLong').click(function(e) {
  e.preventDefault();
  searchLatLong();
});



// function that logs the address info entered in the form
function searchAddress() {
  let street = $('street').val();
  let city = $('city').val();
  let state = $('state').val();
  let zip = $('zip').val();
  console.log(street);
  console.log(city);
  console.log(state);
  console.log(zip);

  //
  // let url =`http://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates?f=json&address=${street}&city=${city}&region=${state}&postal=${zip}`;
  //
  // $.get(url, function(res) {
  //   console.log(res);
  //
  // });
}

// check to see if the submit button is pressed, if it is, stop the even from refreshing the page, and call searchAddress()
$('submit_Address').click(function(e) {
  e.preventDefault();
  searchAddress();
});
