'use strict';

var prime_number_of_divisors = function(n) {
    var divisors = function(n) {
        var divisorsInner = function(start, n) {
            if (start === n) {
                return [n];
            }

            if (n % start === 0) {
                return [start].concat(divisorsInner(start + 1, n));
            } else {
                return [].concat(divisorsInner(start + 1, n));
            }
        };
        return divisorsInner(1, n);
    }(n);

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
    return is_prime(divisors.length);
};


exports.prime_number_of_divisors = prime_number_of_divisors;
