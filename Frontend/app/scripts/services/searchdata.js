'use strict';

/**
 * @ngdoc service
 * @name smartCityFrontEndApp.searchData
 * @description
 * # searchData
 * Service in the smartCityFrontEndApp.
 */
angular.module('smartCityFrontEndApp')
  .service('searchData', function () {
    this.lat = 0;
    this.lon = 0;
    this.address = '';
    this.citySelected = {name : 'Lyon'};
    this.criterias = [];
  });
