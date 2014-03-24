# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems.md#problem-7---integer-palindromes


# FUNCTIONS
def is_int_palindrome(number):
    number = str(number)
    if len(number) <= 1:
        return True

    first_letter = number[0]
    last_letter = number[-1]

    if first_letter == last_letter:
        end = len(number) - 2 + 1
        return is_int_palindrome(number[1:end])

    else:
        return False


# main
def main():
    is_int_palindrome(1)
    is_int_palindrome(42)
    is_int_palindrome(100001)
    is_int_palindrome(999)
    is_int_palindrome(123)


# PROGRAM RUN
if __name__ == '__main__':
    main()
