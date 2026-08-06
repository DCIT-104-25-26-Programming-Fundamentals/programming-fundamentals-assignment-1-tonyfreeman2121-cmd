# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def read_matrix(name="matrix"):
    """
    Prompt the user for the number of rows/columns of a matrix named `name`,
    then read that many rows, each as space-separated integers on one line.
    Returns the matrix as a list of lists.
    """
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
 
    matrix = []
    for i in range(rows):
        while True:
            values = input(f"Enter row {i + 1}: ").split()
            if len(values) != cols:
                print(f"  Expected {cols} values, got {len(values)}. Try again.")
                continue
            matrix.append([int(v) for v in values])
            break
 
    return matrix
 
 
def display_matrix(matrix, title="Matrix"):
    """
    Print a matrix in a neat, aligned grid.
    Column widths are based on the longest number so everything lines up.
    """
    print(f"\n{title}:")
 
    if not matrix:
        print("(empty)")
        return
 
    width = max(len(str(value)) for row in matrix for value in row)
 
    for row in matrix:
        line = "  ".join(str(value).rjust(width) for value in row)
        print(line)
 
 
 
def transpose_matrix(matrix):
    """
    Return the transpose of `matrix`: rows become columns and vice versa.
    An M x N matrix becomes an N x M matrix.
    """
    rows = len(matrix)
    cols = len(matrix[0])
 
    # Build an N x M result matrix filled with zeros first
    result = [[0 for _ in range(rows)] for _ in range(cols)]
 
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
 
    return result
 
 
def add_matrices(matrix_a, matrix_b):
    """
    Return the element-wise sum of two matrices of the same size.
    """
    rows = len(matrix_a)
    cols = len(matrix_a[0])
 
    result = [[0 for _ in range(cols)] for _ in range(rows)]
 
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
 
    return result
 

 
def multiply_matrices(matrix_a, matrix_b):
    """
    Return the matrix product A x B.
    A is M x N, B is N x P, result is M x P.
    """
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])
 
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
 
    for i in range(rows_a):  
        for j in range(cols_b):      
            total = 0
            for k in range(cols_a):  
                total += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = total
 
    return result
 

 
def main():
    print("=" * 50)
    print("MATRIX OPERATIONS")
    print("=" * 50)
 
    while True:
        print("\nChoose an operation:")
        print("  A) Transpose a matrix")
        print("  B) Add two matrices")
        print("  C) Multiply two matrices")
        print("  Q) Quit")
        choice = input("Your choice: ").strip().upper()
 
        if choice == "A":
            m = read_matrix("the matrix")
            display_matrix(m, "Original Matrix")
            display_matrix(transpose_matrix(m), "Transposed Matrix")
 
        elif choice == "B":
            print("\n-- Matrix A --")
            a = read_matrix("Matrix A")
            print("\n-- Matrix B (must be the same size as A) --")
            b = read_matrix("Matrix B")
 
            if len(a) != len(b) or len(a[0]) != len(b[0]):
                print("Error: matrices must be the same size to add them.")
                continue
 
            display_matrix(a, "Matrix A")
            display_matrix(b, "Matrix B")
            display_matrix(add_matrices(a, b), "A + B")
 
        elif choice == "C":
            print("\n-- Matrix A (M x N) --")
            a = read_matrix("Matrix A")
            print("\n-- Matrix B (N x P, rows must equal columns of A) --")
            b = read_matrix("Matrix B")
 
            if len(a[0]) != len(b):
                print("Error: columns of A must equal rows of B to multiply.")
                continue
 
            display_matrix(a, "Matrix A")
            display_matrix(b, "Matrix B")
            display_matrix(multiply_matrices(a, b), "A x B")
 
        elif choice == "Q":
            print("Goodbye!")
            break
 
        else:
            print("Invalid choice, please enter A, B, C, or Q.")
 
 
if __name__ == "__main__":
    main()
 
