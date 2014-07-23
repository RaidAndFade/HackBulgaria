'use strict';

var is_decreasing = function(seq) {
    return seq.map(function(value, index, arr) {
        if (index + 1 >= arr.length) {
            return true;
        }
        return value > arr[index + 1];
    }).every(function(x) {
        return x;
    });
};

exports.is_decreasing = is_decreasing;
