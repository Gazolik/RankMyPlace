'use strict';

/**
 * @ngdoc function
 * @name smartCityFrontEndApp.controller:IndMapCtrl
 * @description
 * # MapCtrl
 * Controller of the smartCityFrontEndApp
 */
angular.module('smartCityFrontEndApp')
  .controller('IndMapCtrl', function ($scope) {
    $scope.displayedView = 0;
    $scope.animateSwitchClass = 'animate-switchLeft';
    $scope.prev = function() {
        $scope.animateSwitchClass = 'animate-switchRight';
        if ($scope.displayedView > 0) {
            $scope.displayedView--;
        }
    };
    $scope.next = function() {
        $scope.animateSwitchClass = 'animate-switchLeft';
        if ($scope.displayedView < 2) {
            $scope.displayedView++;
        }
    };
  });
