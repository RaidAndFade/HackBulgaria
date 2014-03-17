# DocumentationyTestCase
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems.md#problem-17---slope-style-score


# FUNCTIONS
def slope_style_score(list):
    maxElement = max(list)
    minElement = min(list)
    list.remove(maxElement)
    list.remove(minElement)
    return sum(list) / len(list)


# main
def main():
    slope_style_score([94, 95, 95, 95, 90])
    slope_style_score([60, 70, 80, 90, 100])
    slope_style_score([96, 95.5, 93, 89, 92])


# PROGRAM RUN
if __name__ == '__main__':
    main()