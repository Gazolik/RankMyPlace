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
    $scope.profilSelected = null;
    $scope.customProfil = {name : 'Profil Perso', imgPath : 'yeoman.png', coefs : []};
     
    var loadProfils = function (){
      serviceAjax.profils(function(data){
          $scope.profils = data;
          $scope.profils.push($scope.customProfil);
      });
    };
    loadProfils();
     
    var loadCriterias = function (){
      serviceAjax.criterias(function(data) {
         searchData.criterias.length = 0;
         for (var i = 0 ; i < data.length ; ++i){
             $scope.customProfil.coefs.push({name : data[i].name, coef : 5});
             searchData.criterias.push({name : data[i].name, coef : 5, code : data[i].code});          
         }
      });
    };          
    if (searchData.criterias.length === 0){
     loadCriterias();
    }
     
    $scope.showHideDetails = function(){
        $scope.show = ! $scope.show;
        if($scope.show === true){
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
        if (index === $scope.profils.length - 1){
            $scope.show = true;
            $scope.msgCriteres ='Cacher les critères';
        }
    };     
         
  });
