'use strict';

/**
 * @ngdoc function
 * @name smartCityFrontEndApp.controller:MapCtrl
 * @description
 * # MapCtrl
 * Controller of the smartCityFrontEndApp
 */
angular.module('smartCityFrontEndApp')
  .controller('MapCtrl', function ($scope) {
    $scope.displayedView = 0;
    $scope.nextView = function() {
        if ($scope.displayedView === 1) {
            $scope.displayedView = 0;
        }
        else {
            $scope.displayedView = 1;
        }
    };
  });
