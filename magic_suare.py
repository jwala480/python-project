import random

def is_magic_square(n):
    matrix = []

    # Generate matrix with random numbers
    for i in range(n):
        row = []
        for j in range(n):
            num = random.randint(1, 9)
            row.append(num)
        matrix.append(row)

    # Print matrix
    print("Generated Matrix:")
    for row in matrix:
        print(row)

    # Sum of first row
    s = sum(matrix[0])

    # Check row sums
    for row in matrix:
        if sum(row) != s:
            return False

    # Check column sums
    for col in range(n):
        col_sum = 0
        for row in range(n):
            col_sum += matrix[row][col]
        if col_sum != s:
            return False

    # Check main diagonal
    if sum(matrix[i][i] for i in range(n)) != s:
        return False

    # Check secondary diagonal
    if sum(matrix[i][n-i-1] for i in range(n)) != s:
        return False

    return True


n = int(input("Enter size of matrix: "))
result = is_magic_square(n)

if result:
    print("It is a Magic Square")
else:
    print("It is Not a Magic Square")