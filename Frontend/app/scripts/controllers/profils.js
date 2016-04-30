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
    $scope.profils = [];
     
     Array.prototype.keySort = function(key, desc){
         this.sort(function(a, b) {
             var result = desc ? (a[key] < b[key]) : (a[key] > b[key]);
             return result ? 1 : -1;
         });
         return this;
    };
    var loadProfils = function (){
      serviceAjax.profils(function(data){
          $scope.profils = data;
          $scope.profils.keySort('name');
          $scope.profils.push({name : 'Profil Perso', imgPath : 'personal.png', coefs : []});
          $scope.show = false;
          searchData.selectedProfil = 0;
          $scope.msgCriteres ='Afficher les critères';
         if (searchData.criterias.length !== 0){
            $scope.updateCoef($scope.profils[0], 0);
         }
          
      });
    };
    loadProfils();
     
    var loadCriterias = function (){
      serviceAjax.criterias(function(data) {
         searchData.criterias.length = 0;
         for (var i = 0 ; i < data.length ; ++i){
             searchData.criterias.push({name : data[i].name, coef : data[i].coef, code : data[i].code});          
         }
         if ($scope.profils.length !== 0){
            $scope.updateCoef($scope.profils[0], 0);
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
        for (var i = 0 ; i < searchData.criterias.length ; ++i){
            if (i < profil.coefs.length){
                searchData.criterias[i].coef = profil.coefs[i].coef;   
            }
            else{
                searchData.criterias[i].coef = 5;
            }
        }
        searchData.selectedProfil = index;
        if (profil.coefs.length === 0){
            $scope.show = true;
            $scope.msgCriteres ='Cacher les critères';
          }
    }; 
      
         
  });
