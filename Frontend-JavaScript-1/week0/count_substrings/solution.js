'use strict';

var count_substrings = function(haystack, needle) {
    var found = haystack.match(new RegExp(needle, "g"));
    return isNaN(found) ? found.length : 0;
};

exports.count_substrings = count_substrings;
