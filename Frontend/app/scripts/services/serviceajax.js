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
            $http.get('http://501srv-2.insa-lyon.fr:8000/profiles').success(function (data){successFct(data.content.profiles)});
           // $http.get('http://localhost:8000/profiles').success(function (data){successFct(data.content.profiles)});
            /*successFct([{name : 'Etudiant', imgPath : 'images/yeoman.png', coefs : [{name : 'Bruit', coef : 1}, 
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
                       ]);*/
        },
        criterias: function(successFct){
            //$http.get("../Server/app.php?a=profils").success(successFct);
            successFct([{name : 'Bruit'},
                        {name : 'Transport commun'},
                        {name : 'Ecole'}]);
        },
        latlon: function(q, city, successFct){
            var url = 'http://nominatim.openstreetmap.org/search.php?q=' + encodeURI(q) + '&city=' + encodeURI(city) + '&state= France&format=json';
            $http.get(url).success(successFct);
        }
    };
  });
