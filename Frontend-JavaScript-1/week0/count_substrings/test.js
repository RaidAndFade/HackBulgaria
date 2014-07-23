'use strict';

var count_substrings = require('./solution').count_substrings;

exports.TestCountSubstrings = function(test) {
    test.equal(count_substrings("This is a test string", "is"), 2);
    test.equal(count_substrings("babababa", "baba"), 2);
    test.equal(count_substrings("JavaScript is an awesome language to program in!", "o"), 3);
    test.equal(count_substrings("We have nothing in common!", "really?"), 0);
    test.equal(count_substrings("This is this and that is this", "this"), 2);
    test.done();
};
