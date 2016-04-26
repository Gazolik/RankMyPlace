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
    var loadProfilsAndCriterias = function (){
      serviceAjax.profils(function(data){
         $scope.profils = data; 
      });
      serviceAjax.criterias(function(data){
         for (var i = 0 ; i < data.length ; ++i){
             searchData.criterias.push({name : data[i].name, coef : 5}); 
        }
      });
    };    
             
    $scope.loadDetails = function (){
        $scope.show = true;
    }; 
     
    loadProfilsAndCriterias();
  });
