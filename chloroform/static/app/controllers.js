// clients
mainApp.controller('ClientCtrl', [ '$scope', '$http', 'searchService','formService',
		function($scope, $http, searchService,formService) {
			$scope.clientSelected = null;
			$scope.onSelect = function(value){
				formService.setClient($scope.clientSelected);
			};
			$scope.getClients = function(val) {
				formService.setClient(null);
				formService.setForm(null);
				return searchService.searchModel('clients', val);
			};
            $scope.newClientName = null;
            $scope.isNew= false;
            $scope.createClient = function(){
            	$scope.isNew= true;
            	$scope.newClientName = null;
			};
			$scope.saveClient = function(){
				if (!$scope.newClientName)
				{alert("Client name is required!");
				return;
				}
				$http.post('/clients',{name:$scope.newClientName})
				.then(function(){
					alert("Client created successfully.");
				},function(){
					alert("Failed to create new client!");
				})
				.finally(function(){
	            	$scope.isNew= false;
				});
			}
		} ]);

// forms
mainApp.controller('FormCtrl',
				[
						'$scope',
						'$http',
						'formService',
						function($scope, $http, formService) {
							$scope.myAns = null;
							$scope.selectedForm = null;
							$scope.selectedClient =  function(){return formService.getClient();};
							$scope.currentForm = function() {
								return formService.getForm();
								
							};
							$scope.loadForm = function() {
								console.log($scope.selectedForm);
								formService.loadForm($scope.selectedForm.id);
							};
							$scope.getHtml = function(question,ind) {
								return formService.createElement(question,ind);
							}
							$scope.client = function() {
								return formService.getClient();
							}
							$scope.forms = function(){return formService.forms()};
							
						} ]);
