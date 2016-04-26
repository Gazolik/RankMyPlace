'use strict';

describe('Service: searchData', function () {

  // load the service's module
  beforeEach(module('smartCityFrontEndApp'));

  // instantiate service
  var searchData;
  beforeEach(inject(function (_searchData_) {
    searchData = _searchData_;
  }));

  it('should do something', function () {
    expect(!!searchData).toBe(true);
  });

});
