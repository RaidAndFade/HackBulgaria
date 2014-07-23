'use strict';

var sum_of_digits = function(n) {
    return Math.abs(n).toString().split('').reduce(function(a, b) {
        a = parseInt(a);
        b = parseInt(b);
        return a + b;
    });
};

exports.sum_of_digits = sum_of_digits;
