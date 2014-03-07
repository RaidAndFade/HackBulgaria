# Problem 0
#
#     The most annoying problem of all. Write a function,
#     called nth_fibonacci(n) that returns the n-th fibonacci number,
#     given by the argument.
#
# Signature
#
#     def nth_fibonacci(n):
#         #implementation here
#
# Test examples
#
#     >>> nth_fibonacci(1)
#     1
#     >>> nth_fibonacci(2)
#     1
#     >>> nth_fibonacci(3)
#     2
#     >>> nth_fibonacci(10)
#     55


# FUNCTIONS
def nth_fibonacci(number)
  if number <= 2
    number = 1

  else
    nth_fibonacci(number - 1) + nth_fibonacci(number - 2)
  end
end

# PROGRAM RUN
puts nth_fibonacci(1)
puts nth_fibonacci(2)
puts nth_fibonacci(3)
puts nth_fibonacci(10)