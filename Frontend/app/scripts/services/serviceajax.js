'use strict';

/**
 * @ngdoc service
 * @name smartCityFrontEndApp.serviceAjax
 * @description
 * # serviceAjax
 * Factory in the smartCityFrontEndApp.
 */
angular.module('smartCityFrontEndApp')
  .factory('serviceAjax', function ($http) {
    return{
        profils: function(successFct){
            //$http.get("../Server/app.php?a=criterias").success(successFct);
            successFct([{name : 'Etudiant', imgPath : 'images/yeoman.png', coefs : [{name : 'Bruit', coef : 1}, 
                                                                                    {name : 'Transport commun', coef : 2}, 
                                                                                    {name : 'Ecole', coef : 3}]},
                        {name : 'Senior', imgPath : 'images/yeoman.png', coefs : [{name : 'Bruit', coef : 3}, 
                                                                                    {name : 'Transport commun', coef : 2}, 
                                                                                    {name : 'Ecole', coef : 1}]},
                        {name : 'Famille', imgPath : 'images/yeoman.png', coefs : [{name : 'Bruit', coef : 2}, 
                                                                                    {name : 'Transport commun', coef : 3}, 
                                                                                    {name : 'Ecole', coef : 1}]},
                        {name : 'Jeune Actif', imgPath : 'images/yeoman.png', coefs : [{name : 'Bruit', coef : 2}, 
                                                                                    {name : 'Transport commun', coef : 1}, 
                                                                                    {name : 'Ecole', coef : 3}]},
                       ]);
        },
        criterias: function(successFct){
            //$http.get("../Server/app.php?a=profils").success(successFct);
            successFct([{name : 'Bruit', min : 0,max : 5},
                        {name : 'Transport commun', min : 0,max : 8},
                        {name : 'Ecole', min : 0, max : 4}]);
        },
        latlon: function(q, city, successFct){
            var url = 'http://nominatim.openstreetmap.org/search.php?q=' + encodeURI(q) + '&city=' + encodeURI(city) + '&state= France&format=json';
            $http.get(url).success(successFct);
        }
    };
  });
