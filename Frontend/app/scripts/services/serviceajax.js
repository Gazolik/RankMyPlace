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
            //$http.get("../Server/app.php?a=profils").success(successFct);
            successFct([{name : 'Etudiant', imgPath : 'images/yeoman.png'},
                        {name : 'Etudiant', imgPath : 'images/yeoman.png'},
                        {name : 'Etudiant', imgPath : 'images/yeoman.png'},
                        {name : 'Etudiant', imgPath : 'images/yeoman.png'},
                        {name : 'Famille', imgPath : 'images/yeoman.png'}]);
        }
    }
  });
