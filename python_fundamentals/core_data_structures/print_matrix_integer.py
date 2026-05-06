#!/usr/bin/env python3

# Prints a matrix of integers

def print_matrix_integer(matrix=[[]]):
    for row in matrix:

        for numb in range(len(row)):

            if numb != len(row) - 1:
                print("{}".format(row[numb]), end=" ")
            else:
                print("{}".format(row[numb]), end="\n")


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print_matrix_integer(matrix)
