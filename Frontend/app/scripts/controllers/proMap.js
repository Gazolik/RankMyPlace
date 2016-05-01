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
    var oldCritere = '';
    var loadedAreas = [];
    var loadAreas = function (){
      serviceAjax.areas(function(data){
          $scope.areas = data;
          if (searchData.selectedArea === ''){
            searchData.selectedArea = 'lyon1';
          }
      });
    };
    var loadCriterias = function (){
      serviceAjax.criterias(function(data) {
         $scope.criterias = data;
         if (searchData.selectedCritere === '' && data.length > 0){
            searchData.selectedCritere = data[0].code;
         }
      });
    };    
    loadAreas();
    loadCriterias();
    
    $scope.updateMap = function(){
        if (oldCritere !== searchData.selectedCritere){
            loadedAreas.length = 0;
        }
        if (loadedAreas.indexOf(searchData.selectedArea) !== -1){
            return;
        }
        $scope.$broadcast('updateMap', oldCritere !== searchData.selectedCritere);
        oldCritere = searchData.selectedCritere;
        loadedAreas.push(searchData.selectedArea);
    };
  });
