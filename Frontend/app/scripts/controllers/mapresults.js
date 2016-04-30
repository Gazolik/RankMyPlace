'use strict';

/**
 * @ngdoc function
 * @name smartCityFrontEndApp.controller:MapResultsCtrl
 * @description
 * # MapResultsCtrl
 * Controller of the smartCityFrontEndApp
 */
angular.module('smartCityFrontEndApp')
  .controller('MapResultsCtrl', function ($scope, searchData, serviceAjax) {
    var heatmapLayer;
    var map;
    $scope.initMap = function(){
        var heatMapData = {
          max:10,
          data: []
        };
        serviceAjax.heatmap(searchData, function(data){
            for (var i = 0 ; i < data.heatmap.length ; ++i){
                heatMapData.data.push({lat: data.heatmap[i][1], lon:data.heatmap[i][0], rank: data.heatmap[i][2]});
            }

            var baseLayer = L.tileLayer(
              'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
                attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
                maxZoom: 18
              }
            );

            var cfg = {
              radius: 0.001,
              maxOpacity: 0.8, 
              scaleRadius: true, 
              useLocalExtrema: true,
              latField: 'lat',
              lngField: 'lon',
              valueField: 'rank'
            };


            heatmapLayer = new HeatmapOverlay(cfg);

            map = new L.Map('heatmap', {
              center: new L.LatLng(data.center.lat, data.center.lon),
              zoom: data.zoom,
              layers: [baseLayer, heatmapLayer]
            });

            heatmapLayer.setData(heatMapData);
        });
    };
  });
