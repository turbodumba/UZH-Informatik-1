#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work.
# You must not change the names or the list of parameters.
# You may introduce private/protected utility methods though.
class Matrix:

    def __init__(self, matrix):
        if not isinstance(matrix, list) or len(matrix) == 0:
            raise AssertionError
        first = True
        for lists in matrix:
            if not isinstance(lists, list):
                raise AssertionError
            if first:
                first = False
                len_of_all = len(lists)
                if len_of_all == 0:
                    raise AssertionError
            else:
                if not len(lists) == len_of_all:
                    raise AssertionError
            for list_in_list in lists:
                if not (isinstance(list_in_list, int) or isinstance(list_in_list, float)):
                    raise AssertionError
        self.__matrix = matrix
        self.__row = len(matrix)
        self.__columns = len_of_all
        # Implement this function and perform required checks
        # create adequate instance variables and check whether they should be private or public

    # To implement the required functionality, you will also have to implement two more
    # of the special functions that include a double underscore as per the task description.
    def __add__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        if not (self.__row == other.__row and self.__columns == other.__columns):
            raise AssertionError("Not the same rows or columns")
        else:
            liste = []
            for i, outer in enumerate(self.__matrix):
                innerlist = []
                for j, inner in enumerate(outer):
                    innerlist.append(self.__matrix[i][j] + other.__matrix[i][j])
                liste.append(innerlist)
            retmat = Matrix(liste)
            return retmat

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        if not (self.__columns == other.__row):
            raise AssertionError("Columns of first matrix isn't the same as rows of the second one")
        else:
            liste = []
            for i in range(self.__row):
                innerlist = []
                for j in range(other.__columns):
                    res = 0
                    for k in range(other.__row):
                        res += self.__matrix[i][k] * other.__matrix[k][j]
                    innerlist.append(res)
                liste.append(innerlist)
            retmat = Matrix(liste)
            return retmat

        # DO NOT CHANGE the functions below! Consider also implementing __repr__ and __str__ for nice printing
    def __repr__(self):
        return "{}".format(self.__matrix)

    def __str__(self):
        return "Matrix : {}".format(self.__matrix)

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        else:
            return self.__matrix == other.__matrix

    def __hash__(self):
        return hash(tuple([tuple(row) for row in self.__matrix]))


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    M = Matrix([[5, 5], [5, 5]])
    T = Matrix([[5, 6], [8, 5]])
    print(M)
    print(T)
    print(M == T)
    d = {M: "1", T: "2"}
    d.update({M: "3"})
    print(d)
    C = M + T
    print(C)
    D = M * T
    print(D)