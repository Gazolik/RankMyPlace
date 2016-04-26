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
    $scope.min =[];
    $scope.max =[];
     
    var loadProfils = function (){
      serviceAjax.profils(function(data){
         $scope.profils = data; 
      });
    };
    loadProfils();
     
    var loadCriterias = function (){
      serviceAjax.criterias(function(data) {
         searchData.criterias.length = 0;
         for (var i = 0 ; i < data.length ; ++i){
             $scope.min += data[i].min;
             $scope.max += data[i].max;
             searchData.criterias.push({name : data[i].name, coef : 5, range : [data[i].min,data[i].max]});          
         }
      });
    };          
    if (searchData.criterias.length === 0){
     loadCriterias();
    }
     
    
    $scope.updateCoef = function (profil){
      for (var i = 0 ; i < searchData.criterias.length ; ++i){
        searchData.criterias[i].coef = profil.coefs[i].coef;        
      }
    };
     
  });
