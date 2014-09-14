var system = require('system');
var args = system.args;

if (args.length === 1) {
  console.log('Try to pass some arguments when invoking this script!');
} else {
  url = args[1];
  var page = require('webpage').create();

  page.open(url, function(status) {
    if (status !== 'success') {
      console.log('Unable to access network');
    } else {
      var jqversion = page.evaluate(function() {
        return jQuery.fn.jquery;
      });
      console.log(jqversion);
    }
    phantom.exit();
  });

}

