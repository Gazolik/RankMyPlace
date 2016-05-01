'use strict';

/**
 * @ngdoc function
 * @name smartCityFrontEndApp.controller:IndAddressCtrl
 * @description
 * # SearchCtrl
 * Controller of the smartCityFrontEndApp
 */
angular.module('smartCityFrontEndApp')
  .controller('IndAddressCtrl', function ($scope, $rootScope) {
    $scope.displayedView = 0;
    $scope.animateSwitchClass = 'animate-switchLeft';
    $scope.prev = function() {
        if ($scope.displayedView > 0) {
            $scope.animateSwitchClass = 'animate-switchRight';
            $scope.displayedView--;
        }
    };
    $scope.next = function() {
        if ($scope.displayedView < 2) {
            $scope.animateSwitchClass = 'animate-switchLeft';
            if ($scope.displayedView !== 1){
                $scope.displayedView++;
            }
            else{
                $rootScope.$broadcast('getLatLon', function(){$scope.displayedView++;});
            }
        }
    };
  });
