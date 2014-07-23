'use strict';

var sum_of_divisors = function(n) {
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

    return divisors.reduce(function(total, next) {
        total = parseInt(total);
        next = parseInt(next);
        return total + next;
    });
};


exports.sum_of_divisors = sum_of_divisors;
