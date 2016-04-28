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
    $scope.loading = true;
    
    var search = function (){
        serviceAjax.search(searchData, function(data){
            $scope.loading = false;
            $scope.result = data;
            $scope.chartConfig.series[0].data[0] = data.moyenne;
      });
    };
    $scope.chartConfig = {
        options: {
            chart: {
                type: 'solidgauge'
            },
            pane: {
                center: ['50%', '85%'],
                size: '100%',
                startAngle: -90,
                endAngle: 90,
                background: {
                    backgroundColor:'#EEE',
                    innerRadius: '60%',
                    outerRadius: '100%',
                    shape: 'arc'
                }
            },
            tooltip: {
                enabled: false
            }
        },
        series: [{
            data: [5],
            dataLabels: {
	        	format: '<div style="text-align:center"><span style="font-size:25px;color:black;">{y}/1O</span><br/></div>',
                borderWidth: 0,
                useHTML: true,
                y:-40
	        }
        }],
        title: {
            text: 'Note globale',
            y: 130
        },
        yAxis: {
            currentMin: 0,
            currentMax: 10,     
			stops: [
                [0.3, '#DF5353'], // red
	            [0.6, '#DDDF0D'], // yellow
	            [1, '#55BF3B'] // green
			],
			lineWidth: 0,
            tickInterval: 10,
            tickPixelInterval: 100,
            tickWidth: 0,
            labels: {
                y: 16
            }   
        },
        loading: false
    };
    search();
  });
