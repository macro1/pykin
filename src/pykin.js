import angular from 'angular';
import ngResource from 'ng-resource';
/*global module window*/

var app;

ngResource(window, angular);
module.exports = app = angular.module('pykin', ['ngResource']);

app.controller('AuthController', ['$scope', '$resource', ($scope, $resource) => {
  var User = $resource('/api/user');
  $scope.user = User.get();
}]);
