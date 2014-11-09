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
    }
]);
