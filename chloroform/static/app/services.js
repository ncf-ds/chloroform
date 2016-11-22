/**
 * @author salami
 */
mainApp.factory("searchService", [ '$http', function($http) {
	
	// Search given model by name field
	var _searchModel = function(model,searchTerm) {
		return $http.get('/'+model+'/name/'+searchTerm, {
			params : {}
		}).then(function(response) {
			console.log(response);
			return response.data.map(function(item) {
				return item;
			});
		});
	};

	return {
		searchModel : _searchModel,
	};
} ]);
