reporter_view.controller('ContextSearchController', [
    '$scope',
    '$window',
    '$routeParams',
    'contextService',
    function ($scope, $window, $routeParams, contextService) {
        'use strict';
        var question = $routeParams.question,
            answer = $routeParams.answer;

        $scope.reset = function () {
            $scope.context = {};
        }

        contextService.get_context(question, answer).then(function (resp) {
            $scope.reset();
            $scope.context = resp.data;
            console.log($scope.context);
        });
    }
]);
