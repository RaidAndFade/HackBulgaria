'use strict';

var is_prime = require('./solution').is_prime;

exports.TestIsPrime = function(test) {
    test.equal(is_prime(1), false);
    test.equal(is_prime(2), true);
    test.equal(is_prime(8), false);
    test.equal(is_prime(11), true);
    test.equal(is_prime(-10), false);
    test.done();
};
