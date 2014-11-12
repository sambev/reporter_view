/**
* reporter_view Module
*
* Description
*/
reporter_view = angular.module('reporterView', ['ngRoute']);

reporter_view.config([
    '$routeProvider',
    function ($routeProvider) {
        $routeProvider.when('/', {
            templateUrl: '/static/templates/home/index.html'
        })
        .when('/context/:question/:answer', {
            templateUrl: '/static/templates/home/context.html'
        })
        .otherwise({
            redirectTo: '/'
        });
    }
]);

// Thanks to http://ng.malsup.com/#!/titlecase-filter for the filter
reporter_view.filter('titlecase', function() {
    return function(s) {
        s = ( s === undefined || s === null ) ? '' : s;
        return s.toString().toLowerCase().replace( /\b([a-z])/g, function(ch) {
            return ch.toUpperCase();
        });
    };
});

reporter_view.filter('encodeURIComponent', function() {
    return window.encodeURIComponent;
});
