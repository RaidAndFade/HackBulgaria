'use strict';

var sum_of_min_and_max = function(arr) {
    arr.sort(function(a, b) {
        return a - b;
    });
    console.log(arr);
    return arr[0] + arr[arr.length - 1];
};

exports.sum_of_min_and_max = sum_of_min_and_max;
