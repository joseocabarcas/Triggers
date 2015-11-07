'use strict';

// Declare app level module which depends on views, and components
var app = angular.module('app', [
    'ngAnimate' //Directiva que proporciona soporte para animaciones basadas en CSS
]);


/*Configuraciones del modulo de angular para cambiar su referencia( {{}} )
por ( {$$} )  por los conflictos que genera con el manejo de vistas en django*/
app.config(function($interpolateProvider) { 
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});





//run para cargar los headers por defecto al llamar el servicio http
app.run(function ($rootScope, $http) {
    $rootScope.$on('$locationChangeSuccess', function (event, next, current) {
        $http.defaults.headers.get['Content-Type'] = 'application/json;charset=utf-8';
        $http.defaults.headers.post;
    });
    $rootScope.$on('routeChangeError',
            function (event, current, previous) {
//                if (current.locals.data && current.locals.data.resolveError) {
//                    current.locals.$template = $templateCache.get('error.html')
//                    $rootScope.error = current.locals.data.resolveError
//                }
            }
    );
});