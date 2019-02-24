(function () {
  'use strict';

  angular.module('weatherCities', [])

  .controller('cityController', ['$scope', '$log', '$http',
    function($scope, $log, $http) {
    	$scope.alert = {
			type: '',
			message: ''
		};

      $scope.sendCity = function() {     	    
      	  	$http.post('/create', {"name": $scope.name_city, "country_code":$scope.country_code}).
			  then(function(result){			  	
			  	$scope.alert.type    = "success";
			  	$scope.alert.message = "Cidade cadastrada com sucesso!";
			  	
			  }, function(error){
			  	$scope.alert.type    = "danger";
			  	$scope.alert.message = "Cidade inválida!";

			  });
      };

      $scope.getCities = function(){
      	$http.get('/cities').then(function(result){
      		$scope.cities = result.data;
      	}, function(error){
      		$log.log(error);
      	});
      };

      $scope.getCityView = function(city_id) {
      	$http.get('/city/'+city_id).then(function(result){
      		$scope.forecast = result.data;
      	}, function(error){
      		$log.log(error);
      	});
      };

      $scope.getCities();
    }
  ]);

}());