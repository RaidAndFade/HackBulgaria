'use strict';

var list_to_number = function(digitsList) {
    return digitsList.map(function(elem) {
        return elem.toString();
    }).reduce(function(a, b) {
        return a + b;
    });
};

exports.list_to_number = list_to_number;
