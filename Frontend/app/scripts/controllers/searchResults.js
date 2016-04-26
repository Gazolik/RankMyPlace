'use strict';

/**
 * @ngdoc function
 * @name smartCityFrontEndApp.controller:ResultsCtrl
 * @description
 * # ResultsCtrl
 * Controller of the smartCityFrontEndApp
 */
angular.module('smartCityFrontEndApp')
  .controller('SearchResultsCtrl', function ($scope, serviceAjax, searchData) {
    $scope.searchData = searchData;
  });
