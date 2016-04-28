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
           // $http.get('http://501srv-2.insa-lyon.fr:8000/profiles').success(function (data){successFct(data.content.profiles)});
            $http.get('http://localhost:8000/profiles').success(function (data){successFct(data.content.profiles);});
            /*successFct([{name : 'Etudiant', imgPath : 'yeoman.png', coefs : [{name : 'Bruit', coef : 1, code:''}, 
                                                                                    {name : 'Transport commun', coef : 2}, 
                                                                                    {name : 'Ecole', coef : 3}]},
                        {name : 'Senior', imgPath : 'yeoman.png', coefs : [{name : 'Bruit', coef : 3}, 
                                                                                    {name : 'Transport commun', coef : 2}, 
                                                                                    {name : 'Ecole', coef : 1}]},
                        {name : 'Famille', imgPath : 'yeoman.png', coefs : [{name : 'Bruit', coef : 2}, 
                                                                                    {name : 'Transport commun', coef : 3}, 
                                                                                    {name : 'Ecole', coef : 1}]},
                        {name : 'Jeune Actif', imgPath : 'yeoman.png', coefs : [{name : 'Bruit', coef : 2}, 
                                                                                    {name : 'Transport commun', coef : 1}, 
                                                                                    {name : 'Ecole', coef : 3}]},
                       ]);*/
        },
        criterias: function(successFct){
           // $http.get('http://501srv-2.insa-lyon.fr:8000/criterias').success(function (data){successFct(data.content.criteres)});
            $http.get('http://localhost:8000/criterias').success(function (data){successFct(data.content.criteres);});
            /*successFct([{name : 'Bruit'},
                        {name : 'Transport commun'},
                        {name : 'Ecole'}]);*/
        },
        areas: function(successFct){
           // $http.get('http://501srv-2.insa-lyon.fr:8000/criterias').success(function (data){successFct(data.content.criteres)});
            //$http.get('http://localhost:8000/criterias').success(function (data){successFct(data.content.criteres);});
            successFct([{name : 'Lyon 1er', imgPath : 'lyon1.png'},
                        {name : 'Lyon 2ème', imgPath : 'lyon2.png'},
                        {name : 'Lyon 3ème', imgPath : 'lyon3.png'},
                        {name : 'Lyon 4ème', imgPath : 'lyon4.png'},
                        {name : 'Lyon 5ème', imgPath : 'lyon5.png'},
                        {name : 'Lyon 6ème', imgPath : 'lyon6.png'},
                        {name : 'Lyon 7ème', imgPath : 'lyon7.png'},
                        {name : 'Lyon 8ème', imgPath : 'lyon8.png'},
                        {name : 'Lyon 9ème', imgPath : 'lyon9.png'}]);
        },
        search: function(searchData, successFct){
            var args = {criteres : {}, lat : parseFloat(searchData.lat), lon : parseFloat(searchData.lon)};
            for (var i = 0 ; i < searchData.criterias.length ; ++i){
                args.criteres[searchData.criterias[i].code] = parseInt(searchData.criterias[i].coef);          
            }
            // $http.POST('http://501srv-2.insa-lyon.fr:8000/criterias').success(function (data){successFct(data.content.profiles)});
            $http.post('http://localhost:8000/ranking', 'data=' + JSON.stringify(args)).success(function (data){successFct(data.content);});
           // successFct({note : 8});
        },
        latlon: function(q, city, successFct){
            var url = 'http://nominatim.openstreetmap.org/search.php?q=' + encodeURI(q) + '&city=' + encodeURI(city) + '&state= France&format=json';
            $http.get(url).success(successFct);
        }
   //     ranking : {"code": coef, "code2", coef}
    };
  });
