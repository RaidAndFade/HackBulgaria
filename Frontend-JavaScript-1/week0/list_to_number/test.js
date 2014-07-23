'use strict';

var list_to_number = require('./solution').list_to_number;

exports.TestListToNumber = function(test) {
    test.equal(list_to_number([1, 2, 3]), 123);
    test.equal(list_to_number([9, 9, 9, 9, 9]), 99999);
    test.equal(list_to_number([1, 2, 3, 0, 2, 3]), 123023);
    test.done();
};
