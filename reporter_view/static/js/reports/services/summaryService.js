/**
 * @factory summaryService
 * @dependency - $http
 */
reporter_view.factory('summaryService', [
    '$http',
    function ($http) {
        return {
            /**
             * @method get_totals
             * @return {$http promise}
             */
            get_totals: function () {
                return $http.get('/reports/totals')
            },

            /**
             * @method get_question_summaries
             * @return {$http promise}
             */
            get_question_summaries: function() {
                return $http.get('/reports/summary')
            }
        }
    }
]);
