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
  });
