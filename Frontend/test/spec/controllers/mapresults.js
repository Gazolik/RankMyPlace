'use strict';

describe('Controller: MapResultsCtrl', function () {

  // load the controller's module
  beforeEach(module('smartCityFrontEndApp'));

  var MapresultCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    MapresultCtrl = $controller('MapResultsCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(MapresultCtrl.awesomeThings.length).toBe(3);
  });
});
