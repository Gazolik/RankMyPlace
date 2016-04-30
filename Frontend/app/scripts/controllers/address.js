'use strict';

/**
 * @ngdoc function
 * @name smartCityFrontEndApp.controller:AddressCtrl
 * @description
 * # AddressCtrl
 * Controller of the smartCityFrontEndApp
 */
angular.module('smartCityFrontEndApp')
  .controller('AddressCtrl', function ($scope, $route, serviceAjax, searchData) {
    $scope.addressError = false;
    $scope.searchData = searchData;
    $scope.form = {};
    if ($route.current.isPro){
        $scope.pageTitle =  'Quelle adresse vous intéresse ?';
    }
    else{
        $scope.pageTitle =  'Quelle est votre adresse ?';
    }
    
    $scope.$on('getLatLon', function(event, next){
        $scope.form.addressForm.address.$setDirty();
        $scope.form.addressForm.$setSubmitted();
        if($scope.form.addressForm.$valid) {
            serviceAjax.latlon(searchData.address, searchData.citySelected.name, function(data){
                if (data.length > 0){
                    searchData.lat = data[0].lat;
                    searchData.lon = data[0].lon;
                    next();
                }
                else{
                    $scope.addressError = true;
                    $scope.form.addressForm.address.$setPristine();
                }
            });
        }
        
    });
    $scope.citiesData = {
        cities : [
            {name : 'Albigny-sur-Saône'},
            {name : 'Bron'},
            {name : 'Cailloux-sur-Fontaines'},
            {name : 'Caluire-et-Cuire'},
            {name : 'Champagne-au-Mont-d\'Or'},
            {name : 'Charbonnières-les-Bains'},
            {name : 'Charly'},
            {name : 'Chassieu'},
            {name : 'Collonges-au-Mont-d\'Or'},
            {name : 'Corbas'},
            {name : 'Couzon-au-Mont-d\'Or'},
            {name : 'Craponne'},
            {name : 'Curis-au-Mont-d\'Or'},
            {name : 'Dardilly'},
            {name : 'Décines-Charpieu'},
            {name : 'Ecully'},
            {name : 'Feyzin'},
            {name : 'Fleurieu-sur-Saône'},
            {name : 'Fontaines-Saint-Martin'},
            {name : 'Fontaines-sur-Saône'},
            {name : 'Francheville'},
            {name : 'Genay'},
            {name : 'Givors'},
            {name : 'Grigny'},
            {name : 'Irigny'},
            {name : 'Jonage'},
            {name : 'La Mulatière'},
            {name : 'La Tour de Salvagny'},
            {name : 'Limonest'},
            {name : 'Lissieu'},
            {name : 'Lyon'},
            {name : 'Marcy-l\'Etoile'},
            {name : 'Meyzieu'},
            {name : 'Mions'},
            {name : 'Montanay'},
            {name : 'Neuville-sur-Saône'},
            {name : 'Oullins'},
            {name : 'Pierre-Bénite'},
            {name : 'Poleymieux-au-Mont-d\'Or'},
            {name : 'Quincieux'},
            {name : 'Rillieux-la-Pape'},
            {name : 'Rochetaillée-sur-Saône'},
            {name : 'Saint-Cyr-au-Mont-d\'Or'},
            {name : 'Saint-Didier-au-Mont-d\'Or'},
            {name : 'Saint-Fons'},
            {name : 'Saint-Genis-Laval'},
            {name : 'Saint-Genis-les-Ollières'},
            {name : 'Saint-Germain-au-Mont-d\'Or'},
            {name : 'Saint-Priest'},
            {name : 'Saint-Romain-au-Mont-d\'Or'},
            {name : 'Sainte-Foy-lès-Lyon'},
            {name : 'Sathonay-Camp'},
            {name : 'Sathonay-Village'},
            {name : 'Solaize'},
            {name : 'Tassin-la-Demi-Lune'},
            {name : 'Vaulx-en-Velin'},
            {name : 'Vénissieux'},
            {name : 'Vernaison'},
            {name : 'Villeurbanne'}
        ],
    };
  });
