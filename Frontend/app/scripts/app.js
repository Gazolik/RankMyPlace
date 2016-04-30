'use strict';

/**
 * @ngdoc overview
 * @name smartCityFrontEndApp
 * @description
 * # smartCityFrontEndApp
 *
 * Main module of the application.
 */
angular
  .module('smartCityFrontEndApp', [
    'ui.bootstrap',
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch',
    'ui.bootstrap-slider',
    'highcharts-ng', 
    'angularSpinner',
    'leaflet-directive',
    'heatmap'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/ind/address', {
        templateUrl: 'views/indAddress.html',
        controller: 'IndAddressCtrl',
        controllerAs: 'indAddress',
        isPro: false
      })
      .when('/ind/map', {
        templateUrl: 'views/indMap.html',
        controller: 'IndMapCtrl',
        controllerAs: 'indMap',
        isPro: false
      })
      .when('/pro/address', {
        templateUrl: 'views/proAddress.html',
        controller: 'ProAddressCtrl',
        controllerAs: 'proAddress',
        isPro: true
      })
      .when('/pro/map', {
        templateUrl: 'views/proMap.html',
        controller: 'ProMapCtrl',
        controllerAs: 'proMap',
        isPro: true
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl',
        controllerAs: 'about'
      })
      .when('/', {
        templateUrl: 'views/home.html',
        controller: 'HomeCtrl',
        controllerAs: 'home'
      })
      .otherwise({
        redirectTo: '/'
      });
  }).config(['$httpProvider', function ($httpProvider) {
        //Reset headers to avoid OPTIONS request (aka preflight)
        $httpProvider.defaults.headers.common = {};
        $httpProvider.defaults.headers.post = {};
        $httpProvider.defaults.headers.put = {};
        $httpProvider.defaults.headers.patch = {};
}]);

angular.element(document).ready(function() {
      angular.bootstrap(document, ['smartCityFrontEndApp']);
    });