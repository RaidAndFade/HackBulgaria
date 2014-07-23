'use strict';

var prime_number_of_divisors = require('./solution').prime_number_of_divisors;

exports.TestPrimeNUmberOfDivisors = function(test) {
    test.equal(prime_number_of_divisors(7), true);
    test.equal(prime_number_of_divisors(8), false);
    test.equal(prime_number_of_divisors(9), true);
    test.done();
};
