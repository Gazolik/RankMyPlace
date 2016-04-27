'use strict';

/**
 * @ngdoc directive
 * @name smartCityFrontEndApp.directive:loading
 * @description
 * # loading
 */
angular.module('smartCityFrontEndApp')
    .directive('loading', function () {
        return {
           restrict: 'A',
           transclude: true,
           template: '<div><span ng-show="loading" us-spinner="{radius:30, width:8, length: 16}"></span></span><div ng-hide="loading" ng-transclude></div></div>',
           replace: true,
           scope:{
               loading: '=loading'
           }
        };
    });
