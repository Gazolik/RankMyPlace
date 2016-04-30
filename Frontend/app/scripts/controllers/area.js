'use strict';

/**
 * @ngdoc function
 * @name smartCityFrontEndApp.controller:AreactrlCtrl
 * @description
 * # AreactrlCtrl
 * Controller of the smartCityFrontEndApp
 */
angular.module('smartCityFrontEndApp')
  .controller('AreasCtrl', function ($scope, serviceAjax, searchData) {
    $scope.searchData = searchData;
    
    $scope.clickOnBubble = function(index, code){
        searchData.selectedArea = index;
        searchData.areaCode = code;
    };
    
    var loadAreas = function (){
      serviceAjax.areas(function(data){
          $scope.areas = data;
          searchData.selectedArea = 0;
          searchData.areaCode = $scope.areas[0].code;
      });
    };
    loadAreas();
  });
