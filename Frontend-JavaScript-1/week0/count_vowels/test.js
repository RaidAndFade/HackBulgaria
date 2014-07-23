'use strict';

var count_vowels = require('./solution').count_vowels;

exports.TestCountVowels = function(test) {
    test.equal(count_vowels("JavaScript"), 3);
    test.equal(count_vowels("Theistareykjarbunga"), 8);
    test.equal(count_vowels("grrrrgh!"), 0);
    test.equal(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"), 22);
    test.equal(count_vowels("A nice day to code!"), 8);
    test.done();
};
