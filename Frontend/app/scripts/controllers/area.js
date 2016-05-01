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
    $scope.mainAreas = [];
    $scope.clickOnBubble = function(code){
        searchData.selectedArea = code;
    };
    
    var loadAreas = function (){
      serviceAjax.areas(function(data){
          $scope.areas = data;
          for (var i = 0 ; i < data.length ; ++i){
              if (data[i].imgPath !== ''){
                  $scope.mainAreas.push(data[i]);  
              }
          }
          if (searchData.selectedArea === ''){
            searchData.selectedArea = 'lyon1';
          }
      });
    };
    loadAreas();
  });
