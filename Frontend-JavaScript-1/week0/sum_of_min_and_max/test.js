'use strict';

var sum_of_min_and_max = require('./solution').sum_of_min_and_max;

exports.TestSumOfMinAndMax = function(test) {
    test.equal(sum_of_min_and_max([1, 2, 3, 4, 5, 6, 8, 9]), 10);
    test.equal(sum_of_min_and_max([-10, 5, 10, 100]), 90);
    test.equal(sum_of_min_and_max([1]), 2);
    test.done();
};
