'use strict';

/**
 * @ngdoc function
 * @name smartCityFrontEndApp.controller:ProfilsCtrl
 * @description
 * # ProfilsCtrl
 * Controller of the smartCityFrontEndApp
 */
 angular.module('smartCityFrontEndApp')
  .controller('ProfilsCtrl', function ($scope, serviceAjax, searchData, $route) {
     
    $scope.searchData = searchData;  
    $scope.profils = [];
    $scope.allCriterias = 5;     
    $scope.mode = false;
     
    angular.element('[data-toggle="tooltip"]').tooltip(); 
      
    Array.prototype.getIndexBy = function (name, value) {
        for (var i = 0; i < this.length; i++) {
            if (this[i][name] === value) {
                return i;
            }
        }
        return -1;
    };
    
    var loadProfils = function (){
      serviceAjax.profils(function(data){
          $scope.profils = data;
          for (var i = 0 ; i < $scope.profils.length ; ++i){
            $scope.profils[i].coefs.keySort('code');      
          }
          $scope.profils.keySort('name');
          $scope.profils.push({name : 'Profil Perso', imgPath : 'personal.png', coefs : []});
          $scope.show = false;
          $scope.msgCriteres ='Afficher les critères';
          if (searchData.criterias.length !== 0 && searchData.selectedProfil === -1){
            $scope.updateCoef($scope.profils[0], 0);
          }
          
      });
    };
    loadProfils();
     
    var loadCriterias = function (){      
      serviceAjax.criterias(function(data) {
         searchData.criterias.length = 0;
         for (var i = 0 ; i < data.length ; ++i){
             searchData.criterias.push({groupe : data[i].groupe, name : data[i].name, description : data[i].description, coef : data[i].coef, code : data[i].code, type : data[i].type, dist : null, dens : null, slider : false, show : null});   
         }
         searchData.criterias.keySort('groupe');
         var groups = [];          
         var showCrit = []; 
         for (var j = 0 ; j < searchData.criterias.length ; ++j){
             if(!groups.includes(searchData.criterias[j].groupe)){
                groups.push(searchData.criterias[j].groupe);
                showCrit.push({show : true});
             }
             else{
                 searchData.criterias[j].groupe = '';
             }
             searchData.criterias[j].show = showCrit[showCrit.length-1];
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
            var indexCriteria = profil.coefs.getIndexBy('code', searchData.criterias[i].code);
            if (indexCriteria !== -1){
                searchData.criterias[i].coef = profil.coefs[indexCriteria].coef;   
            }
            else{
                searchData.criterias[i].coef = 5;
            }
        }
        searchData.selectedProfil = index;
        if (profil.coefs.length === 0){
            $scope.show = true;
            $scope.msgCriteres ='Cacher les critères';
            $scope.showCrit.show = false;
          }
    };
     
   /*   
    if(searchData.selectedProfil === $scope.profils.length-1 ){ 
        $scope.$watch('allCriterias', function() {
            for (var i = 0 ; i < searchData.criterias.length ; ++i){
               searchData.criterias[i].coef = $scope.allCriterias;
             }
        });
    }*/
     
    $scope.verifyType = function (criteriaType, sliderType){
        var show = false;
        if((criteriaType === sliderType) || (criteriaType === 'dist_dens_based') ){
            show = true;
        }
        return show;
    };
     
    if ($route.current.showReglage){
        $scope.mode = true;
    }
         
  });
