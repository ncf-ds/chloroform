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
