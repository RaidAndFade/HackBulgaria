## Problem 0

The most annoying problem of all. Write a function, called ```nth_fibonacci(n)``` that returns the n-th fibonacci number, given by the argument.

### Signature

```python
def nth_fibonacci(n):
    #implementation here
```

### Test examples

```
>>> nth_fibonacci(1)
1
>>> nth_fibonacci(2)
1
>>> nth_fibonacci(3)
2
>>> nth_fibonacci(10)
55
>>>
```

### Solution

```
Enter a number: 6
Fibonacci result: 8
```

## Problem 1

Given an integer, write a function, called ```sum_of_digits(n)``` that calculates the sum of the digits of n.

If a negative number is given, the function should work as if it was possitive.

For example, if n is 1325132435356, the digit's sum is 43.
If n is -10, the sum is 1 + 0 = 1

Keep in mind that in Python, there is a special operator for integer division:

```
>>> 5 / 2
2.5
>>> 5 // 2
2
```

### Signature

```python
def sum_of_digits(n):
    # implementation
```

### Test examples

```
>>> sum_of_digits(1325132435356)
43
>>> sum_of_digits(123)
6
>>> sum_of_digits(6)
6
>>> sum_of_digits(-10)
1
```

### Solution

```
Enter a number: 12345
Sum of digits: 15
```

## Problem 2

Given an array of integers, write a function, called ```sum_of_min_and_max(arr)```, that calculates and returns the sum of the largest and the smallest integers in the array.

Don't bother for the case when the array is empty.

### Signature

```python
def sum_of_min_and_max(arr):
    # implementation
```

### Test examples
```
>>> sum_of_min_and_max([1,2,3,4,5,6,8,9])
10
>>> sum_of_min_and_max([-10,5,10,100])
90
>>> sum_of_min_and_max([1])
2
```

### Solution

```
Given list
5 6 7 8 10 15 -5 -2 1
Min of list: -5
Max of list: 15

Sum of min and max of list: 10
```

## Problem 3

Given an integer, write a function, called ```sum_of_divisors(n)``` that calculates the sum of all divisors of n.

For example, the divisors of 8 are 1,2,4 and 8 and ```1 + 2 + 4 + 8 = 15```
The divisors of 7 are 1 and 7, which makes the sum = 8

### Signature

```python
def sum_of_divisors(n):
    # implementation
```

### Test examples

```
>>> sum_of_divisors(8)
15
>>> sum_of_divisors(7)
8
>>> sum_of_divisors(1)
1
>>> sum_of_divisors(1000)
2340
```

### Solution

```
Enter a number: 8
Sum of divisors: 15
```

## Problem 4

Given an integer, write a function, called ```is_prime(n)``` which returns True if n is a prime number. You should handle the case with negative numbers too.

A primer number is a number, that is divisible only by 1 and itself.

1 is not considered to be a prime number. [If you are curious why, find out here.](http://www.youtube.com/watch?v=IQofiPqhJ_s)

### Signature

```python
def is_prime(n):
    # implementation
```

### Test examples

```
>>> is_prime(1)
False
>>> is_prime(2)
True
>>> is_prime(8)
False
>>> is_prime(11)
True
>>> is_prime(-10)
False
```

### Solution

```
Enter a number: 11
Prime? True
```

## Problem 5

Given an integer, write a function, called ```prime_number_of_divisors(n)``` which returns True if the number of divisors of n is a prime number. False otherwise.

For example, the divisors of 8 are 1,2,4 and 8, a total of 4. 4 is not a prime.
The divisors of 9 are 1,3 and 9, a total of 3, which is a prime number.

### Signature

```python
def prime_number_of_divisors(n):
    # Implementation
```

### Test examples

```
>>> prime_number_of_divisors(7)
True
>>> prime_number_of_divisors(8)
False
>>> prime_number_of_divisors(9)
True
```

### Solution

```
Enter a number: 9
Prime number of divisors: True
```

## Problem 6

Write a function, called ```sevens_in_a_row(arr, n)```, which takes an array of integers ```arr``` and a number ```n > 0```

The function returns True, __if there are n consecutive sevens__ in ```arr```

For example, if ```arr``` is [10,8,7,6,7,7,7,20,-7] and n is 3, the function should return True. Otherwise, it returns False

### Signature

```python
def sevens_in_a_row(arr, n)
```

### Test examples

```
>>> sevens_in_a_row([10,8,7,6,7,7,7,20,-7], 3)
True
>>> sevens_in_a_row([1,7,1,7,7], 4)
False
>>> sevens_in_a_row([7,7,7,1,1,1,7,7,7,7], 3)
True
>>> sevens_in_a_row([7,2,1,6,2], 1)
True
```

### Solution

```
Enter numbers. Type (S) to stop.
1
6
7
2
7
7
7
s

How many sevens in a row do you want to find: 3
3 sevens in a row? True
```