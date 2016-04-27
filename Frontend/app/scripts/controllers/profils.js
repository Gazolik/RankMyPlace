'use strict';

/**
 * @ngdoc function
 * @name smartCityFrontEndApp.controller:ProfilsCtrl
 * @description
 * # ProfilsCtrl
 * Controller of the smartCityFrontEndApp
 */
 angular.module('smartCityFrontEndApp')
  .controller('ProfilsCtrl', function ($scope, serviceAjax, searchData) {
     
    $scope.searchData = searchData;
    $scope.show = false;
    $scope.msgCriteres = 'Afficher les critères';
    $scope.min =[];
    $scope.max =[];
    $scope.profilSelected = null;
     
    var loadProfils = function (){
      serviceAjax.profils(function(data){
         var profilPerso = {name : 'Profil Perso', imgPath : 'images/yeoman.png', coefs : [{name : 'Bruit', coef : 5},
                                                                                           {name : 'Transport commun', coef : 5},
                                                                                           {name : 'Ecole', coef : 5}]
                           };
          $scope.profils = data;
          $scope.profils.push(profilPerso);
      });
    };
    loadProfils();
     
    var loadCriterias = function (){
      serviceAjax.criterias(function(data) {
         searchData.criterias.length = 0;
         for (var i = 0 ; i < data.length ; ++i){
             $scope.min += data[i].min;
             $scope.max += data[i].max;
             searchData.criterias.push({name : data[i].name, coef : 5, range : [data[i].min,data[i].max]});          
         }
      });
    };          
    if (searchData.criterias.length === 0){
     loadCriterias();
    }
     
    $scope.loadDetails = function(){
        $scope.show = ! $scope.show;
        if($scope.msgCriteres === 'Afficher les critères'){
            $scope.msgCriteres = 'Cacher les critères';
        }
        else{
            $scope.msgCriteres ='Afficher les critères';
        }
    };
     
    
    $scope.updateCoef = function (index){
      for (var i = 0 ; i < searchData.criterias.length ; ++i){
        searchData.criterias[i].coef = $scope.profils[index].coefs[i].coef;        
      }
        $scope.profilSelected = index;     
    };
    
         
  });
