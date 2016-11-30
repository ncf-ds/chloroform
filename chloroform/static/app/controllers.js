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
            $scope.showClientNew = false;
            $scope.clientNew= null;
            $scope.createModel = function(name) {
                return $http.post('/clients/', {
                    name: name
                }).then(function(response){
                    console.log(response);
                    return response.data.map(function(item){
                        return item;
                    });
                });
            };
		} ]);
