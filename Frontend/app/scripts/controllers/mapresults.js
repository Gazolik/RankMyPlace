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
    $scope.displayTooltip = 'none';
    $scope.topTooltip = '0px';
    $scope.leftTooltip = '0px';
    $scope.tooltipValue = 0;
    var heatMapData = {
          max:1000,
          min:0,
          data: []
        };
    $scope.initMap = function(){ 
       heatMapData.data.length = 0;
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
          latField: 'lat',
          lngField: 'lon',
          valueField: 'rank'
        };


        heatmapLayer = new HeatmapOverlay(cfg);

        map = new L.Map('heatmap', {
              center: new L.LatLng(45.73532,4.82857),
              zoom: 14,
              layers: [baseLayer, heatmapLayer]
            });
    };
    
    var setData = function(data){
        for (var i = 0 ; i < data.heatmap.length ; ++i){
            heatMapData.data.push({lat: data.heatmap[i][1], lon:data.heatmap[i][0], rank: data.heatmap[i][2]*100});
        }

        map.setZoom(data.zoom);
        map.panTo(new L.LatLng(data.center.lat, data.center.lon));
        heatmapLayer.setData(heatMapData);
    };
    $scope.updateMap = function(){
        serviceAjax.heatmapCriterias(searchData, setData);
    };
    $scope.$on('updateMap', function(event, clear){
        if (clear === true){
            heatMapData.data.length = 0;
        }
        serviceAjax.heatmapCriteria(searchData.selectedArea, searchData.selectedCritere, setData);
    });
    
    $scope.showTooltip = function(event) {
      var x = event.offsetX;
      var y = event.offsetY;
      var value = heatmapLayer._heatmap.getValueAt({x: x, y: y});
      $scope.displayTooltip = 'block';
      $scope.topTooltip = (event.clientY - 40) + 'px';
      $scope.leftTooltip = (event.clientX - 20) + 'px';
      $scope.tooltipValue = value/100;
    };
    
    $scope.hideTooltip = function() {
      $scope.displayTooltip = 'none';
    };
  });
