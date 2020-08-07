require.config({
    "baseUrl": "./",
    "paths": {
      //"jquery": "//ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min",
      "daterangepicker":"++plone++collective.pat_daterangepicker/daterangepicker-compiled"
    }
});


// Load the main app module to start the app
// require(["app/main"]);
require(["jquery","moment","daterangepicker"], function($,moment,daterangepicker) {
    //the semantic ui code is loaded up also.
    $(function() {
        $('.pat-daterangepicker').daterangepicker();
    });
});