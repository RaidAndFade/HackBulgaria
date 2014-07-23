'use strict';

var is_number_balanced = function(n) {
    var i, j;
    var leftSum = 0;
    var rightSum = 0;
    var stringN = n.toString().split("").map(function(elem) {
        return parseInt(elem, 10);
    });
    console.dir(stringN);
    for (i = 0; i < stringN.length / 2; i++) {
        leftSum += stringN[i];
    }

    for (j = stringN.length / 2 | 0; j < stringN.length; j++) {
        rightSum += stringN[j];
    }
    return leftSum == rightSum;
};

exports.is_number_balanced = is_number_balanced;
