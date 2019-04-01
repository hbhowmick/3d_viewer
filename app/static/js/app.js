import Config from '../../config.py'

let config = new Config();

function searchURL() {
  let url = $('url').val();
  console.log(url);
}

// check to see if the submit button is pressed, if it is, stop the event from refreshing the page, and call searchURL()
$('submit_url').click(function(e) {
  e.preventDefault();
  searchURL();
});
