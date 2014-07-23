'use strict';

var nth_fib = require('./solution').nth_fib;

exports.TestFibOne = function(test) {
    test.equal(nth_fib(1), 1);
    test.done();
};

exports.TestFibTwo = function(test) {
    test.equal(nth_fib(2), 1);
    test.done();
};

exports.TestFibThree = function(test) {
    test.equal(nth_fib(3), 2);
    test.done();
};

exports.TestFibTen = function(test) {
    test.equal(nth_fib(10), 55);
    test.done();
};
