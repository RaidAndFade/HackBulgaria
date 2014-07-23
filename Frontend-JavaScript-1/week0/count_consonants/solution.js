'use strict';

var count_consonants = function(string) {
    return string.match(/[bcdfghjklmnpqrstvwxz]/gi).length;
};

exports.count_consonants = count_consonants;
