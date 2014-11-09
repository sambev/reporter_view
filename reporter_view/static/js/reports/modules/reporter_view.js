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
        .otherwise({
            redirectTo: '/'
        });
    }
]);
