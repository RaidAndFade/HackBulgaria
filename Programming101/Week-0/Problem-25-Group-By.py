# Problem 25 - Group By
#
# This problem is from the Python 2013 course in FMI You can see the original problem statement here - http://2013.fmi.py-bg.net/tasks/2
#
# Implement a function, called groupby(func, seq) which returns a dictionary, which keys are determined by the func argument.
#
# The values are items from seq
#
# Signature
#
# def groupby(func, seq):
#     # Implementation
# Test examples
#
# >>> groupby(lambda x: x % 2, [0,1,2,3,4,5,6,7])
# {0: [0, 2, 4, 6], 1: [1, 3, 5, 7]}
# >>> groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12])
# {'even': [2, 8, 10, 12], 'odd': [1, 3, 5, 9]}
# >>> groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7])
# {0: [0, 3, 6], 1: [1, 4, 7], 2: [2, 5]}

# FUNCTIONS
def groupby(func, seq):
    outputDic = { }

    for element in seq:
        key = func(element)

        if key not in outputDic.keys():
            outputDic[key] = [element]

        else:
            outputDic[key].append(element)

    return outputDic

# main
def main():
    print(groupby(lambda x: x % 2, [0,1,2,3,4,5,6,7]))
    print(groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]))
    print(groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))

# PROGRAM RUN
main()