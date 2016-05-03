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
        isPro: false,
        showReglage : true
      })
      .when('/ind/map', {
        templateUrl: 'views/indMap.html',
        controller: 'IndMapCtrl',
        controllerAs: 'indMap',
        isPro: false,
        showReglage : false
      })
      .when('/pro/address', {
        templateUrl: 'views/proAddress.html',
        controller: 'ProAddressCtrl',
        controllerAs: 'proAddress',
        isPro: true, 
        showReglage : false
      })
      .when('/pro/map', {
        templateUrl: 'views/proMap.html',
        controller: 'ProMapCtrl',
        controllerAs: 'proMap',
        isPro: true, 
        showReglage : false
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
        $httpProvider.defaults.useXDomain = true;
		delete $httpProvider.defaults.headers.common["X-Requested-With"];
        $httpProvider.defaults.headers.common = {};
        $httpProvider.defaults.headers.post = {};
        $httpProvider.defaults.headers.put = {};
        $httpProvider.defaults.headers.patch = {};
}]);

Array.prototype.keySort = function(key, desc){
     this.sort(function(a, b) {
         var result = desc ? (a[key] < b[key]) : (a[key] > b[key]);
         return result ? 1 : -1;
     });
     return this;
};