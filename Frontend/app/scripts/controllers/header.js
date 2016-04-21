'use strict';

/**
 * @ngdoc function
 * @name smartCityFrontEndApp.controller:HeaderCtrl
 * @description
 * # HeaderCtrl
 * Controller of the smartCityFrontEndApp
 */
angular.module('smartCityFrontEndApp')
  .controller('HeaderCtrl', function ($scope, $location) {
    $scope.isActive = function (viewLocation) {
        var active = (viewLocation === $location.path());
        return active;
    };
  });
