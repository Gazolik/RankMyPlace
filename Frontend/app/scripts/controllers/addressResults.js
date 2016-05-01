'use strict';

/**
 * @ngdoc function
 * @name smartCityFrontEndApp.controller:AddressResultsCtrl
 * @description
 * # ResultsCtrl
 * Controller of the smartCityFrontEndApp
 */
angular.module('smartCityFrontEndApp')
  .controller('AddressResultsCtrl', function ($scope, $route, serviceAjax, searchData) {
    $scope.searchData = searchData;
    $scope.loading = true;
    var color = ['#FF6666', '#FFCC66', '#CCFF66', '#66FF66', '#66FFCC', '#66CCFF', '#CC66FF', '#8000FF', '#0080FF', '#008080'];
    $scope.gaugesConfig = [];
    $scope.nbGauges = 0;
    $scope.barClass = '';
    $scope.titleGauges = 'Note globale';
    
    var search = function (index, criterias, lat, lon){
        serviceAjax.search(criterias, lat, lon, function(data){
            $scope.loading = false;
            $scope.gaugesConfig[index].series[0].data[0] = Math.round(data.moyenne*100)/100;
            for (var i = 0 ; i < data.notes.length ; ++i){
                if (data.notes[i].note !== -1){
                    $scope.barConfig.series[index].data.push({y:Math.round(data.notes[i].note*100)/100, color:color[i%10]});
                    $scope.barConfig.xAxis.categories.push(data.notes[i].name);
                }
            }
            $scope.barConfig.size.height = (400 + index * 10 * criterias.length);
            $scope.$broadcast('highchartsng.reflow');
      });
    };
    
    var addGaugeConfig = function(graphName, serieName){
        $scope.gaugesConfig.push({
            options: {
                chart: {
                    type: 'solidgauge',
                    height: 210,
                    width: 290
                },
                pane: {
                    center: ['50%', '85%'],
                    size: '140%',
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
                    format: '<div style="text-align:center"><span style="font-size:16px;color:black;">{y}/1O</span><br/></div>',
                    borderWidth: 0,
                    useHTML: true,
                    y:-30
                }
            }],
            title: {
                text: graphName,
                y:15,
                floating:true
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
        });
        $scope.barConfig.series.push({
            showInLegend: false,
            name : serieName,
            data: []
        });
    };
    
    $scope.barConfig = {
        options: {
            chart: {
                type: 'bar'
            }
        },
        yAxis: {
            currentMin: 0,
            tickInterval: 2,
            currentMax: 10,
            title: {
                text: null
            }
        },
        xAxis: {
            categories: [],
            title: {
                text: null
            }
        },
        series: [],
        title: {
            text: null
        },
        size: {
            height: 400,
            width : 1000
        },
        loading: false
    };
    
    if ($route.current.isPro){
        $scope.titleGauges = 'Note par profil';
        serviceAjax.profils(function(data){
            data.keySort('name');
            $scope.nbGauges = data.length;
            for (var i = 0 ; i < data.length ; ++i){
                addGaugeConfig(data[i].name, data[i].name);
                search(i, data[i].coefs, searchData.lat, searchData.lon);
            }
        });
    }
    else{
        $scope.nbGauges = 1;
        addGaugeConfig('', 'score');
        search(0, searchData.criterias, searchData.lat, searchData.lon);
    }
    
  });
