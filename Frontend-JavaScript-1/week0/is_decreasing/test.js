'use strict';

var is_decreasing = require("./solution").is_decreasing;

exports.TestIsDecreasing = function(test) {
    test.equal(is_decreasing([5, 4, 3, 2, 1]), true);
    test.equal(is_decreasing([1, 2, 3]), false);
    test.equal(is_decreasing([100, 50, 20]), true);
    test.equal(is_decreasing([1, 1, 1, 1]), false);
    test.done();
};
