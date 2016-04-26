'use strict';

/**
 * @ngdoc function
 * @name smartCityFrontEndApp.controller:ProfilsCtrl
 * @description
 * # ProfilsCtrl
 * Controller of the smartCityFrontEndApp
 */
 angular.module('smartCityFrontEndApp')
  .controller('ProfilsCtrl', function ($scope, serviceAjax) {
    
    var loadProfils = function (){
      serviceAjax.profils(function(data){
         $scope.profils = data; 
      });
    };    
    loadProfils();
     
  /* var slider = new Slider('#coef', {tooltip: 'always'}); */
        
    $scope.show = false;
    $scope.loadDetails = function (){
        $scope.show = true;
        serviceAjax.criterias(function(data){
            $scope.criterias = data; 
        });
       // slider();
    }; 
    
    
  });
