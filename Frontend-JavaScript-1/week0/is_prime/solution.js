'use strict';

var is_prime = function(n) {
    if (n < 2 || n != Math.round(n)) {
        return false;
    }
    var isPrime = true;

    for (var i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) {
            isPrime = false;
        }
    }
    return isPrime;
};

exports.is_prime = is_prime;
