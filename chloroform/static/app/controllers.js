/**
 * @author salami
 */
//clients
mainApp.controller('ClientCtrl', ['$scope', '$http',
function($scope, $http) {
	$scope.clientSelected = null;
	$scope.onSelect = function(){
		console.log(clientSelected);
	};
	$scope.getClients = function(val) {
	    return $http.get('/clients/name/'+val, {
	      params: {
	      }
	    }).then(function(response){
	    	console.log(response);
	      return response.data.map(function(item){
	        return item;
	      });
	    });
	  };
	
}]);



