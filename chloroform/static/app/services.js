/**
 * @author salami
 */
mainApp.factory("searchService", [ '$http', function($http) {
	
	// Search given model by textsearchable field defined in models
	var _searchModel = function(model,searchTerm) {
		return $http.get('/'+model+'/search/'+searchTerm, {
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
