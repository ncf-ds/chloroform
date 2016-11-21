/**
 * @author salami
 */
// clients
mainApp.controller('ClientCtrl', [ '$scope', '$http', 'searchService',
		function($scope, $http, searchService) {
			$scope.clientSelected = null;
			$scope.onSelect = function() {
				console.log(clientSelected);
			};
			$scope.getClients = function(val) {
				return searchService.searchModel('clients', val);
			};

		} ]);
