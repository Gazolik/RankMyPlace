'use strict';

describe('Controller: AddressCtrl', function () {

  // load the controller's module
  beforeEach(module('smartCityFrontEndApp'));

  var AddressCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    AddressCtrl = $controller('AddressCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(AddressCtrl.awesomeThings.length).toBe(3);
  });
});
