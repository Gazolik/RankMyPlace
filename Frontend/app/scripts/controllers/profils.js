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
    $scope.customProfil = {name : 'Profil Perso', imgPath : 'personal.png', coefs : []};
     
    var loadProfils = function (){
      serviceAjax.profils(function(data){
          $scope.profils = data;
          $scope.profils.push($scope.customProfil);
          $scope.show = false;
          searchData.selectedProfil = 0;
          $scope.msgCriteres ='Afficher les critères';
          
      });
    };
    loadProfils();
     
    var loadCriterias = function (){
      serviceAjax.criterias(function(data) {
         searchData.criterias.length = 0;
         for (var i = 0 ; i < data.length ; ++i){
             $scope.customProfil.coefs.push({name : data[i].name, coef : 5});
             searchData.criterias.push({name : data[i].name, coef : $scope.customProfil.coefs[i].coef, code : data[i].code});          
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
     
    $scope.updateCoef = function (profil, index){
        for (var i = 0 ; i < Math.min(searchData.criterias.length, profil.coefs.length) ; ++i){
            searchData.criterias[i].coef = profil.coefs[i].coef;        
        }
        searchData.selectedProfil = index;
        if ($scope.profilSelected === $scope.customProfil){
            $scope.show = true;
            $scope.msgCriteres ='Cacher les critères';
          }
    }; 
      
         
  });
