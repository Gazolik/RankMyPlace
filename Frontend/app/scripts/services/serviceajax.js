'use strict';

/**
 * @ngdoc service
 * @name smartCityFrontEndApp.serviceAjax
 * @description
 * # serviceAjax
 * Factory in the smartCityFrontEndApp.
 */
angular.module('smartCityFrontEndApp')
  .factory('serviceAjax', function ($http, $q) {
    return{
        profils: function(successFct){
            //$http.get("../Server/app.php?a=criterias").success(successFct);
            successFct([{name : 'Etudiant', imgPath : 'images/yeoman.png', coefs : [{name : 'Bruit', coef : 3}, 
                                                                                    {name : 'Transport commun', coef : 8}, 
                                                                                    {name : 'Ecole', coef : 5}]},
                        {name : 'Senior', imgPath : 'images/yeoman.png', coefs : [{name : 'Bruit', coef : 3}, 
                                                                                    {name : 'Transport commun', coef : 8}, 
                                                                                    {name : 'Ecole', coef : 5}]},
                        {name : 'Famille', imgPath : 'images/yeoman.png', coefs : [{name : 'Bruit', coef : 3}, 
                                                                                    {name : 'Transport commun', coef : 8}, 
                                                                                    {name : 'Ecole', coef : 5}]},
                        {name : 'Jeune Actif', imgPath : 'images/yeoman.png', coefs : [{name : 'Bruit', coef : 3}, 
                                                                                    {name : 'Transport commun', coef : 8}, 
                                                                                    {name : 'Ecole', coef : 5}]},
                       ]);
        },
        criterias: function(successFct){
            //$http.get("../Server/app.php?a=profils").success(successFct);
            successFct([{name : 'Bruit'},
                        {name : 'Transport commun'},
                        {name : 'Ecole'}]);
        }
    }
  });
