'use strict';

/**
 * @ngdoc function
 * @name smartCityFrontEndApp.controller:MainCtrl
 * @description
 * # SearchCtrl
 * Controller of the smartCityFrontEndApp
 */
angular.module('smartCityFrontEndApp')
  .controller('SearchCtrl', function ($scope, serviceAjax) {
    var loadProfils = function (){
      serviceAjax.profils(function(data){
         $scope.profils = data; 
      });
    };
    loadProfils();
  });
