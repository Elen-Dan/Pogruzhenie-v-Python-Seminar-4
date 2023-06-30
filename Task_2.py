'''
Напишите функцию для транспонирования матрицы
'''

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def print_matrix(input_matrix):
    for col in input_matrix:
        for row in col:
            print(row, "\t", end="")
        print()

def matrix_transpositions(input_matrix):
    new_matrix = []
    list_in_matrix = []
    count_start = 0
    count_stop = 1
    while count_start < len(matrix):
        for column in input_matrix:
            for row in column[count_start:count_stop:]:
                list_in_matrix.append(row)
        new_matrix.append(list_in_matrix)
        list_in_matrix = []
        count_start += 1
        count_stop += 1
    return new_matrix
print("\nБыло:\n")
print_matrix(matrix)
print("\nСтало:\n")
print_matrix(matrix_transpositions(matrix))