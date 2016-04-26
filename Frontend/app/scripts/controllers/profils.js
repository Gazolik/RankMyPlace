'use strict';

/**
 * @ngdoc function
 * @name smartCityFrontEndApp.controller:ProfilsCtrl
 * @description
 * # ProfilsCtrl
 * Controller of the smartCityFrontEndApp
 */
 angular.module('smartCityFrontEndApp')
  .controller('ProfilsCtrl', function ($scope, serviceAjax, searchData) {
    $scope.searchData = searchData;
    $scope.show = false;
    var loadProfils = function (){
      serviceAjax.profils(function(data){
         $scope.profils = data; 
      });
    };   
    var loadCriterias = function (){
      serviceAjax.criterias(function(data){
         searchData.criterias.length = 0;
         for (var i = 0 ; i < data.length ; ++i){
             searchData.criterias.push({name : data[i].name, coef : 5}); 
        }
      });
    };   
             
    $scope.loadDetails = function (){
        $scope.show = true;
    }; 
     
    loadProfils();
    if (searchData.criterias.length === 0){
        loadCriterias();
    }
  });
