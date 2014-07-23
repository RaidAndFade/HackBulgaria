'use strict';

var count_vowels = function(string) {
    return string.match(/[aeiou]/gi).length;
};

exports.count_vowels = count_vowels;
