/* RequireJS configuration */
/* global module:true */

(function() {
  'use strict';

  var requirejsOptions = {
    baseUrl: './',
    optimize: 'none',
    paths: {
       "daterangepicker": "bower_components/daterangepicker/daterangepicker",
       "moment": "bower_components/moment/min/moment.min",
       'mockup-bundles-daterangepicker': 'js/bundles/pattern',
        // Add any other dependencies here. For external libraries, also add
        // them to bower.json
        "jquery":                       "bower_components/jquery/dist/jquery",
        "jquery.browser":               "bower_components/jquery.browser/dist/jquery.browser",
        "logging":                      "bower_components/logging/src/logging",
        "pat-base":                     "bower_components/patternslib/src/core/base",
        "pat-compat":                   "bower_components/patternslib/src/core/compat",
        "pat-jquery-ext":               "bower_components/patternslib/src/core/jquery-ext",
        "pat-logger":                   "bower_components/patternslib/src/core/logger",
        "pat-mockup-parser":            "bower_components/patternslib/src/core/mockup-parser",
        "pat-parser":                   "bower_components/patternslib/src/core/parser",
        "pat-registry":                 "bower_components/patternslib/src/core/registry",
        "pat-utils":                    "bower_components/patternslib/src/core/utils",
        "underscore":                   "bower_components/underscore/underscore"

    },
    "shim": {
        "logging": { "exports": "logging" },
        "daterangepicker": {
      deps: [
        "jquery",
        "moment",
        "underscore"
      ]
    }
    }, wrapShim: true
  };

  if (typeof exports !== 'undefined' && typeof module !== 'undefined') {
    module.exports = requirejsOptions;
  }
  if (typeof requirejs !== 'undefined' && requirejs.config) {
    requirejs.config(requirejsOptions);
    require(["pat-registry", "pat-daterangepicker"], function(registry, pattern) {
    // your pattern is found via it's name in the filesystem, starting from the
    // requireJS baseUrl option: "pat-daterangepicker"
    window.patterns = registry;
    $(document).ready(function() {
        registry.init();
    });
});
  }

}());