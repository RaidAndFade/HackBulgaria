'use strict';

var is_number_balanced = require('./solution').is_number_balanced;

exports.TestIsIntPalindrome = function(test) {
    test.equal(is_number_balanced(9), true);
    test.equal(is_number_balanced(11), true);
    test.equal(is_number_balanced(13), false);
    test.equal(is_number_balanced(121), true);
    test.equal(is_number_balanced(4518), true);
    test.equal(is_number_balanced(28471), false);
    test.equal(is_number_balanced(1238033), true);
    test.done();
};
