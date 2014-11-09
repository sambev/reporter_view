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
             * @method get_summary_for_numeric_question
             * @param {String} question e.g. 'Who are you with?'
             * @return {$http promise}
             */
            get_summary_for_numeric_question: function (question) {
                var url = '/reports/summary/numeric/' + encodeURIComponent(question),
                    req = $http.get(url);

                return req;
            },

            /**
             * @method get_summary_for_token_question
             * @param {String} question e.g. 'Who are you with?'
             * @return {$http promise}
             */
            get_summary_for_token_question: function (question) {
                var url = '/reports/summary/token/' + encodeURIComponent(question),
                    req = $http.get(url);

                return req;
            },

            /**
             * @method get_summary_for_location_question
             * @param {String} question e.g. 'Who are you with?'
             * @return {$http promise}
             */
            get_summary_for_location_question: function (question) {
                var url = '/reports/summary/location/' + encodeURIComponent(question),
                    req = $http.get(url);

                return req;
            },

            /**
             * @method get_sleep_summary
             * @return {$http promise}
             */
            get_sleep_summary: function () {
                return $http.get('/sleep/summary/')
            }
        }
    }
]);
