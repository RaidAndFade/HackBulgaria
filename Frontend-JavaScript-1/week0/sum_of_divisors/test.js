'use strict';

var sum_of_divisors = require('./solution').sum_of_divisors;

exports.TestSumOfDivisors = function(test) {
    test.equal(sum_of_divisors(8), 15);
    test.equal(sum_of_divisors(7), 8);
    test.equal(sum_of_divisors(1), 1);
    test.equal(sum_of_divisors(1000), 2340);
    test.done();
};
