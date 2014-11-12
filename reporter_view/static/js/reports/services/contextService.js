reporter_view.factory('contextService', [
    '$http',
    function ($http) {
        'use strict';
        /**
         * @class contextService
         * @type {Object}
         */
        var contextService = {};

        /**
         * @method get_context
         * @param {string} question
         * @param {string} answer
         * @return {$http Promise}
         */
        contextService.get_context = function (question, answer) {
            var req = $http({
                method: 'GET',
                url: '/reports/context/' + encodeURIComponent(question) + '/' + encodeURIComponent(answer)
            });

            return req;
        };

        return contextService;
    }
]);
