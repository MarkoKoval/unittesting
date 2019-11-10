
def quick_sort(collection):
    if not iter(collection):
        raise Exception
    length = len(collection)
    if length <= 1:
        return collection
    else:
        pivot = collection.pop()
        greater, lesser = [], []
        for element in collection:
            if element > pivot:
                greater.append(element)
            else:
                lesser.append(element)
        return quick_sort(lesser) + [pivot] + quick_sort(greater)

def linear_search(sequence, target):
    for index, item in enumerate(sequence):
        if item == target:
            return index
    return None

class UnsortedException(Exception):
    def __str__(self):
        return "Array is unsorted"
def binary_search(sorted_collection, item):

    if sorted_collection != sorted(sorted_collection):
        raise UnsortedException
       # return None
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        midpoint = left + (right - left) // 2
        current_item = sorted_collection[midpoint]
        if current_item == item:
            return midpoint
        elif item < current_item:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return None


class  EmptyCoordinatesException(Exception):
    def __str__(self):
        return "No coordinates passed"


def points_to_polynomial(coordinates):
    if coordinates == []:
        raise EmptyCoordinatesException
    try:

        check = 1
        more_check = 0
        d = coordinates[0][0]
        for j in range(len(coordinates)):
            if j == 0:
                continue
            if d == coordinates[j][0]:
                more_check += 1
                solved = "x=" + str(coordinates[j][0])
                if more_check == len(coordinates) - 1:
                    check = 2
                    break
                elif more_check > 0 and more_check != len(coordinates) - 1:
                    check = 3
                else:
                    check = 1

        if len(coordinates) == 1 and coordinates[0][0] == 0:
            check = 2
            solved = "x=0"
    except Exception:
        check = 3

    x = len(coordinates)

    if check == 1:
        count_of_line = 0
        matrix = []
        # put the x and x to the power values in a matrix
        while count_of_line < x:
            count_in_line = 0
            a = coordinates[count_of_line][0]
            count_line = []
            while count_in_line < x:
                count_line.append(a ** (x - (count_in_line + 1)))
                count_in_line += 1
            matrix.append(count_line)
            count_of_line += 1

        count_of_line = 0
        # put the y values into a vector
        vector = []
        while count_of_line < x:
            count_in_line = 0
            vector.append(coordinates[count_of_line][1])
            count_of_line += 1

        count = 0

        while count < x:
            zahlen = 0
            while zahlen < x:
                if count == zahlen:
                    zahlen += 1
                if zahlen == x:
                    break
                bruch = (matrix[zahlen][count]) / (matrix[count][count])
                for counting_columns, item in enumerate(matrix[count]):
                    # manipulating all the values in the matrix
                    matrix[zahlen][counting_columns] -= item * bruch
                # manipulating the values in the vector
                vector[zahlen] -= vector[count] * bruch
                zahlen += 1
            count += 1

        count = 0
        # make solutions
        solution = []
        while count < x:
            solution.append(vector[count] / matrix[count][count])
            count += 1

        count = 0
        solved = "f(x)="

        while count < x:
            remove_e = str(solution[count]).split("E")
            if len(remove_e) > 1:
                solution[count] = remove_e[0] + "*10^" + remove_e[1]
            solved += "x^" + str(x - (count + 1)) + "*" + str(solution[count])
            if count + 1 != x:
                solved += "+"
            count += 1

        return solved

    elif check == 2:
        return solved
    else:
        return "The program cannot work out a fitting polynomial."


def minor(matrix, row, column):
    minor = matrix[:row] + matrix[row + 1 :]
    minor = [row[:column] + row[column + 1 :] for row in minor]
    return minor


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]

    res = 0
    for x in range(len(matrix)):
        res += matrix[0][x] * determinant(minor(matrix, 0, x)) * (-1) ** x
    return res

def string_reverse(string):
    return string[::-1] if type(string) == str else None

def is_palindrome(str):
    start_i = 0
    end_i = len(str) - 1
    while start_i < end_i:
        if str[start_i] == str[end_i]:
            start_i += 1
            end_i -= 1
        else:
            return False
    return True

def naivePatternSearch(mainString, pattern):
    if type(mainString) != str:
        return None
    patLen = len(pattern)
    strLen = len(mainString)
    position = []
    for i in range(strLen - patLen + 1):
        match_found = True
        for j in range(patLen):
            if mainString[i + j] != pattern[j]:
                match_found = False
                break
        if match_found:
            position.append(i)
    return position

def euclid(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def checkTriangleValidity(a, b, c):
    # check condition
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    else:
        return True