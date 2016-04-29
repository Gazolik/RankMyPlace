'use strict';

/**
 * @ngdoc function
 * @name smartCityFrontEndApp.controller:HomeCtrl
 * @description
 * # HomeCtrl
 * Controller of the smartCityFrontEndApp
 */
angular.module('smartCityFrontEndApp')
  .controller('HomeCtrl', function () {
    angular.element('#homeCarousel').carousel({
        interval: 4000,
        cycle: true
        });
  });
