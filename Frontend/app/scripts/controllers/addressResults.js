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
    $scope.titleProfilBar = 'Notes pour votre profil';
    $scope.tabIndex = 0;
    
    Array.prototype.countValid = function () {
        var count = 0;
        for (var i = 0; i < this.length; i++) {
            if (this[i].coef === 0) {
                count++;
            }
        }
        return count;
    };
    
    var search = function (showAllCriterias, index, criterias, lat, lon){
        serviceAjax.search(criterias, lat, lon, function(data){
            $scope.loading = false;
            data.notes.keySort('name');
            $scope.gaugesConfig[index].series[0].data[0] = Math.round(data.moyenne*100)/100;
            var show = true;
            for (var i = 0 ; i < data.notes.length ; ++i){
                show = true;
                if (data.notes[i].note === -1 && !showAllCriterias){
                    show = false;
                }
                else if(data.notes[i].note === -1){
                   data.notes[i].note = 1;
                }
                if (show){
                    if (index === 0){
                        $scope.barAddressConfig.series[index].data.push({y:Math.round(data.notes[i].note*100)/100, color:color[i%10]});
                        $scope.barAddressConfig.xAxis.categories.push(data.notes[i].name);
                    }
                    
                    $scope.barProfilConfig.series[index].data.push({y:data.notes[i].satisfaction, color:color[showAllCriterias ? index : i%10]});
                    $scope.barProfilConfig.xAxis.categories.push(data.notes[i].name);
                }
            }
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
                    format: '<div style="text-align:center"><span style="font-size:16px;color:black;">{y}/10</span><br/></div>',
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
        if ($scope.barAddressConfig.series.length === 0){
            $scope.barAddressConfig.series.push({
                showInLegend: false,
                name : 'score',
                data: []
            });
        }
        $scope.barProfilConfig.series.push({
            showInLegend: false,
            name : serieName,
            data: []
        });
    };
    
    $scope.barAddressConfig = {
        options: {
            chart: {
                type: 'bar',
                marginLeft:150
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
        loading: false
    };
    
    $scope.barProfilConfig = {
        options: {
            chart: {
                type: 'bar'
            },
            tooltip: {
                formatter: function () {
                    var ret = '';
                    if (this.series.name !== 'score'){
                        ret += '<b>' + this.series.name + '</b><br/>'; 
                    }
                    if (this.point.y < 0){
                        return ret + this.point.category + '<br/>Insatisfaction : <b>' + Math.abs(this.point.y) + '%'; 
                    }
                    return ret + this.point.category + '<br/>Satisfaction : <b>' + this.point.y + '%'; 
                },  
            },
        },
        yAxis: {
            currentMin: -100,
            tickInterval: 20,
            currentMax: 100,
            title: {
                text: null
            },
            labels: {
                crop: false,
                formatter: function () {
                    var ret = Math.abs(this.value) + '%';
                    if (this.value === -80){
                        ret += '<br/><b>Insastisfait</b>';
                    }
                    else if (this.value === 80){
                        ret += '<br/><b>Sastisfait</b>';
                    }
                    else if (this.value === 0){
                        ret += '<br/><b>Indifférent</b>';
                    }
                    return ret;
                }
            }
        },
        xAxis: {
            categories: [],
            reversed: false,
            labels: {
                step: 1
            }
        },
        series: [],
        title: {
            text: null
        },
        plotOptions: {
            series: {
                stacking: 'normal'
            }
        },
        loading: false
    };
    
    if ($route.current.isPro){
        $scope.titleGauges = 'Note par profil';
        $scope.titleProfilBar = 'Notes pour les différents profils';
        $scope.satisfactionGraphHeight = {height:'1200px'};
        serviceAjax.profils(function(data){
            data.keySort('name');
            $scope.nbGauges = data.length;
            for (var i = 0 ; i < data.length ; ++i){
                addGaugeConfig(data[i].name, data[i].name);
                search(true, i, data[i].coefs, searchData.lat, searchData.lon);
            }
        });
    }
    else{
        $scope.nbGauges = 1;
        addGaugeConfig('', 'score');
        $scope.satisfactionGraphHeight = {height:(50 * searchData.criterias.countValid()) + 'px'};
        search(false, 0, searchData.criterias, searchData.lat, searchData.lon);
    }
    
  });
