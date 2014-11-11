/**
 * @controller SummaryController
 * @dependency - $scope
 * @dependency - summaryService
 */
reporter_view.controller('SummaryController', [
    '$scope',
    'summaryService',
    function ($scope, summaryService) {
        summaryService.get_totals().then(function (resp) {
            $scope.totals = resp.data;
        });

        summaryService.get_question_summaries().then(function (resp) {
            $scope.tokens = resp.data.tokens;
            $scope.numerics = resp.data.numeric;
            $scope.location = resp.data.locations;
        });
    }
]);
