'use strict';

describe('Controller: AreactrlCtrl', function () {

  // load the controller's module
  beforeEach(module('smartCityFrontEndApp'));

  var AreactrlCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    AreactrlCtrl = $controller('AreactrlCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(AreactrlCtrl.awesomeThings.length).toBe(3);
  });
});
