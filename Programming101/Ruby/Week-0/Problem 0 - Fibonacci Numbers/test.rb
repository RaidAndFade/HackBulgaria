# Unit test for Problem 0 - Fibonacci Numbers


# IMPORTS
require_relative "solution"
require "test/unit"


# TESTS
class MyTestCase < Test::Unit::TestCase
    def test_1
        assert_equal(1, nth_fibonacci(1))
    end

    def test_2
        assert_equal(1, nth_fibonacci(2))
    end

    def test_3
        assert_equal(2, nth_fibonacci(3))
    end

    def test_10
        assert_equal(55, nth_fibonacci(10))
    end
end
