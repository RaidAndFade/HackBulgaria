'use strict';

var sum_of_digits = require('./solution').sum_of_digits;

exports.TestSumDigits = function(test) {
    test.equal(sum_of_digits(1325132435356), 43);
    test.equal(sum_of_digits(123), 6);
    test.equal(sum_of_digits(6), 6);
    test.equal(sum_of_digits(-10), 1);
    test.done();
};
