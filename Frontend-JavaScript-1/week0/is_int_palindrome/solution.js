'use strict';

var is_int_palindrome = function(n) {
    var stringN = n.toString();
    return stringN === stringN.split("").reverse().join("");
};


exports.is_int_palindrome = is_int_palindrome;
