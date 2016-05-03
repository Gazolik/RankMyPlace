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
    $scope.criteriasWarning = [];
    
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
            for (var i = 0 ; i < data.notes.length ; ++i){
                if (data.notes[i].note !== -1){
                    if (index === 0){
                        $scope.barAddressConfig.series[index].data.push({y: Math.round(data.notes[i].note*100)/100, 
                                                                         color:color[i%10],
                                                                         density: data.notes[i].density,
                                                                         closest: data.notes[i].closest, 
                                                                         closestDis: data.notes[i].closestDist});
                        $scope.barAddressConfig.xAxis.categories.push(data.notes[i].name);
                    }
                    if (data.notes[i].satisfaction !== -101){
                        $scope.barProfilConfig.series[index].data.push({y: data.notes[i].satisfaction, 
                                                                        color: color[showAllCriterias ? index : i%10],
                                                                        density: data.notes[i].density,
                                                                        closest: data.notes[i].closest, 
                                                                        closestDis: data.notes[i].closestDist});
                        $scope.barProfilConfig.xAxis.categories.push(data.notes[i].name);
                    }
                }
                else if($scope.criteriasWarning.indexOf(data.notes[i].name) === -1){
                    $scope.criteriasWarning.push(data.notes[i].name);
                }
            }
            $scope.$broadcast('highchartsng.reflow');
      });
    };
    
    var tooltipInfo = function(data){
        var ret = '';
        if (data.closest !== null){
            ret += '<br/><br/>Distance avec l\'entité la plus proche : <b>' + data.closestDis + '</b> mètres<br/>';
            if (data.closest.data.name !== undefined){
                ret += '&nbsp;&nbsp;&nbsp;&nbsp;-<i> Nom : ' + data.closest.data.name + '</i><br/>';
            }
            if (data.closest.data.type !== undefined){
                ret += '&nbsp;&nbsp;&nbsp;&nbsp;-<i> Thème : ' + data.closest.data.type + '</i>';
            }
        }
        if (data.density !== null && data.density.value !== null && data.density.radius !== null){
            ret += '<br/><br/>Densité : <b>' + data.density.value + '</b> entité';
            ret += (data.density.value <= 1 ? '' : 's');
            ret += ' dans un rayon de <b>' + data.density.radius + ' mètre';
            ret += (data.density.radius <= 1 ? '' : 's');
        }
        return ret + '</b>';
    };
    
    var addGaugeConfig = function(graphName, serieName, address){
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
                name : address,
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
            },
            tooltip: {
                useHTML: true,
                formatter: function () {
                    var ret = '<div class="text-center"><b>' + this.series.name + '</b><br/><small>' + this.point.category + '</small></div><br/>';
                    return ret + 'Note : <b>' + this.point.y + '/10</b>' + tooltipInfo(this.point); 
                },  
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
                useHTML: true,
                formatter: function () {
                    var ret = '<div class="text-center"><b>' + this.series.name + '</b><br/><small>' + this.point.category + '</small></div><br/>';
                    if (this.point.y < -20){
                        ret += 'Insatisfaction : <b>';
                    }
                    else if (this.point.y > 20){
                        ret += 'Satisfaction : <b>';
                    }
                    else{
                        ret += 'Indifférence : <b>';
                    }
                    return ret + Math.abs(this.point.y) + '%</b>' + tooltipInfo(this.point); 
                },  
            }
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
                        ret += '<br/><b>Insatisfait</b>';
                    }
                    else if (this.value === 80){
                        ret += '<br/><b>Satisfait</b>';
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
                addGaugeConfig(data[i].name, data[i].name, searchData.address);
                search(true, i, data[i].coefs, searchData.lat, searchData.lon);
            }
        });
    }
    else{
        $scope.nbGauges = 1;
        addGaugeConfig('', searchData.profilName, searchData.address);
        $scope.satisfactionGraphHeight = {height:(50 * searchData.criterias.countValid()) + 'px'};
        search(false, 0, searchData.criterias, searchData.lat, searchData.lon);
    }
    
  });
