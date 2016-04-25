'use strict';

describe('Controller: ProfilsCtrl', function () {

  // load the controller's module
  beforeEach(module('smartCityFrontEndApp'));

  var ProfilsCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    ProfilsCtrl = $controller('ProfilsCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(ProfilsCtrl.awesomeThings.length).toBe(3);
  });
});
