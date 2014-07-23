'use strict';

var number_to_list = require('./solution').number_to_list;

exports.TestNumberToList = function(test) {
    test.deepEqual(number_to_list(123), [1, 2, 3]);
    test.deepEqual(number_to_list(99999), [9, 9, 9, 9, 9]);
    test.deepEqual(number_to_list(123023), [1, 2, 3, 0, 2, 3]);
    test.done();
};
