/**
 * @author salami
 */
mainApp.factory("searchService", [ '$http', function($http) {
	
	// Search given model by textsearchable field defined in models
	var _searchModel = function(model,searchTerm) {
		return $http.get('/'+model+'/search/'+searchTerm, {
			params : {}
		}).then(function(response) {
			return response.data.map(function(item) {
				return item;
			});
		});
	};
	return {
		searchModel : _searchModel,
	};
} ]);

//Form Service
mainApp.factory("formService", [ '$http','$sce', function($http,$sce) {
	
	var _client = null;
	var _getClient = function(){
		return _client;
	};
	var _setClient = function(client){
		_client = client;
	};
	var _form = null;
	var _forms = null;
	var _getForm = function(){
		return _form;
	};
	var _setForm = function(form){
		 _form = form;
	};
	var _loadForm = function(formID) {
		 $http.get('/forms/'+formID+'/edit', {
			params : {}
		}).then(function(response) {
			_form = response.data;
		});
//		$http.get('/static/data.json', {
//			params : {}
//		}).then(function(response) {
//			_form = response.data;
//		});
	};
	var _createElement = function(question,index){
		q = question;
		var regExp = /\${([^}]+)\}/g;
		var match =null;
		var order = index +1;
		q.html = order+'- '+q.text;
		madlibs = ['Display','Palermos Pepperoni Pizza','Palermos Sausage Pizza','Palermos Cheese Pizza','Shampoo'];
		while (match = regExp.exec(q.html)){
			var madlibItems = "item for item in q.madlibs";
			var selectElement = '<select  ng-model="myAns">';
			selectElement += '<option value="1">'+ q.madlibs[match[1]].text +'</option>';
			angular.forEach(madlibs, function(value, key) {
				  if (value != q.madlibs[match[1]].text){
					  selectElement += '<option value="">'+ value +'</option>';
				  };
				});
			selectElement += '</select>';			
			q.html = q.html.replace(match[0],selectElement);	
		};
		return $sce.trustAsHtml(q.html);
	};
	
    $http.get('/forms', {
			params : {}
		}).then(function(response) {
			_forms = response.data;
		});


	return {
		getForm : _getForm,
		loadForm: _loadForm,
		setForm: _setForm,
		createElement: _createElement,
		getClient:_getClient,
		setClient:_setClient,
		forms : function(){return _forms;}
	};
} ]);
