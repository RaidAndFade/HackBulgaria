'use strict';

var number_to_list = function(n) {
    return n.toString().split('').map(function(element) {
        return parseInt(element, 10);
    });
};

exports.number_to_list = number_to_list;
