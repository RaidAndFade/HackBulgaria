# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems2.md#problem-34---is-sudoku-solved


# FUNCTIONS
def sudoku_solved(sudoku):
    columns = [] * 9
    rows = [0] * 9
    is_solved = False
    subsquares = [0] * 9
    needed = [[1, 2, 3, 4, 5, 6, 7, 8, 9]] * 9
    sudoku_list = []

    for i in range(9):
        sudoku_list += sudoku[i]
        for j in range(9):
            columns.append(sudoku[j][i])

    for i in range(82):
        if i < 10:
            columns[i] = columns[i * 9:i * 9 + 9]
        else:
            columns.pop()

    for j in range(9):
        if j < 3:
            c = 0
        elif j >= 3 and j < 6:
            c = 18
        else:
            c = 36
        subsquares[j] = (
            sudoku_list[j * 3 + c:j * 3 + 3 + c]
            + sudoku_list[j * 3 + 9 + c:j * 3 + 12 + c]
            + sudoku_list[j * 3 + 18 + c:j * 3 + 21 + c]
        )

    for i in range(9):
        rows[i] = sorted(sudoku[i])
        columns[i] = sorted(columns[i])
        subsquares[i] = sorted(subsquares[i])

    if subsquares == columns == rows == needed:
        is_solved = True
    else:
        is_solved = False

    return is_solved


# main
def main():
    sudoku_solved([[4, 5, 2, 3, 8, 9, 7, 1, 6],
                        [3, 8, 7, 4, 6, 1, 2, 9, 5],
                        [6, 1, 9, 2, 5, 7, 3, 4, 8],
                        [9, 3, 5, 1, 2, 6, 8, 7, 4],
                        [7, 6, 4, 9, 3, 8, 5, 2, 1],
                        [1, 2, 8, 5, 7, 4, 6, 3, 9],
                        [5, 7, 1, 8, 9, 2, 4, 6, 3],
                        [8, 9, 6, 7, 4, 3, 1, 5, 2],
                        [2, 4, 3, 6, 1, 5, 9, 8, 7]])
    sudoku_solved([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9]])

# PROGRAM RUN
if __name__ == '__main__':
    main()
