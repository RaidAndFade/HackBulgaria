'use strict';

var is_increasing = require('./solution').is_increasing;

exports.TestIsIncreasing = function(test) {
    test.equal(is_increasing([1, 2, 3, 4, 5]), true);
    test.equal(is_increasing([1]), true);
    test.equal(is_increasing([5, 6, -10]), false);
    test.equal(is_increasing([1, 1, 1, 1]), false);
    test.done();
};
