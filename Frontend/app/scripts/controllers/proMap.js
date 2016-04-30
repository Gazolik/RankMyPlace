'use strict';

/**
 * @ngdoc function
 * @name smartCityFrontEndApp.controller:MapCtrl
 * @description
 * # MapCtrl
 * Controller of the smartCityFrontEndApp
 */
angular.module('smartCityFrontEndApp')
  .controller('ProMapCtrl', function ($scope, searchData, serviceAjax) {
    $scope.searchData = searchData;
    var loadAreas = function (){
      serviceAjax.areas(function(data){
          $scope.areas = data;
          searchData.selectedArea = 'lyon1';
      });
    };
    var loadCriterias = function (){
      serviceAjax.criterias(function(data) {
         $scope.criterias = data;
         searchData.selectedCritere = data[0].code;
      });
    };    
    loadAreas();
    loadCriterias();
    
    $scope.updateMap = function(){
        $scope.$broadcast('updateMap');
    };
  });
