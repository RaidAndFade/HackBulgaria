'use strict';

var nth_fib = function(n) {
    if (n <= 2) {
        return 1;
    } else {
        return nth_fib(n - 1) + nth_fib(n - 2);
    }
};

exports.nth_fib = nth_fib;
