'use strict';

var is_int_palindrome = require('./solution').is_int_palindrome;

exports.TestIsIntPalindrome = function(test) {
    test.equal(is_int_palindrome(1), true);
    test.equal(is_int_palindrome(42), false);
    test.equal(is_int_palindrome(100001), true);
    test.equal(is_int_palindrome(999), true);
    test.equal(is_int_palindrome(123), false);
    test.done();
};
