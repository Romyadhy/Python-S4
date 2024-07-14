def strassen(matrixA, matrixB, display_steps=False):
    n = len(matrixA)
    
    # Base case: when the matrix is 1x1, perform standard multiplication
    if n == 1:
        return [[matrixA[0][0] * matrixB[0][0]]]
    
    # Split matrices into quadrants
    mid = n // 2
    A11 = [row[:mid] for row in matrixA[:mid]]
    A12 = [row[mid:] for row in matrixA[:mid]]
    A21 = [row[:mid] for row in matrixA[mid:]]
    A22 = [row[mid:] for row in matrixA[mid:]]
    
    B11 = [row[:mid] for row in matrixB[:mid]]
    B12 = [row[mid:] for row in matrixB[:mid]]
    B21 = [row[:mid] for row in matrixB[mid:]]
    B22 = [row[mid:] for row in matrixB[mid:]]

    # Display split matrices
    if display_steps:
        print("Splitting matrix A into A11, A12, A21, A22:")
        print("A11 =", A11)
        print("A12 =", A12)
        print("A21 =", A21)
        print("A22 =", A22)
        print("\nSplitting matrix B into B11, B12, B21, B22:")
        print("B11 =", B11)
        print("B12 =", B12)
        print("B21 =", B21)
        print("B22 =", B22)

    # Calculate the 7 products recursively
    M1 = strassen(matrix_sub(A12, A22), matrix_add(B21, B22), display_steps)
    M2 = strassen(matrix_add(A11, A22), matrix_add(B11, B22), display_steps)
    M3 = strassen(matrix_sub(A11, A21), matrix_add(B11, B12), display_steps)
    M4 = strassen(matrix_add(A11, A12), B22, display_steps)
    M5 = strassen(A11, matrix_sub(B12, B22), display_steps)
    M6 = strassen(A22, matrix_sub(B21, B11), display_steps)
    M7 = strassen(matrix_add(A21, A22), B11, display_steps)

    # Display the products M1 through M7
    if display_steps:
        print("\nCalculating products M1 to M7:")
        print("M1 =", M1)
        print("M2 =", M2)
        print("M3 =", M3)
        print("M4 =", M4)
        print("M5 =", M5)
        print("M6 =", M6)
        print("M7 =", M7)

    # Calculate the 4 quadrants of the final matrix
    C11 = matrix_add(matrix_sub(matrix_add(M1, M2), M4), M6)
    C12 = matrix_add(M4, M5)
    C21 = matrix_add(M6, M7)
    C22 = matrix_sub(matrix_add(M2, M5), matrix_add(M3, M7))

    # Display the result quadrants
    if display_steps:
        print("\nCalculating the result matrix:")
        print("C11 =", C11)
        print("C12 =", C12)
        print("C21 =", C21)
        print("C22 =", C22)

    # Combine the 4 quadrants into a single matrix
    new_matrix = []
    for i in range(mid):
        new_matrix.append(C11[i] + C12[i])
    for i in range(mid):
        new_matrix.append(C21[i] + C22[i])

    return new_matrix

# Helper functions to add and subtract matrices
def matrix_add(matrixA, matrixB):
    return [[matrixA[i][j] + matrixB[i][j] for j in range(len(matrixA[0]))] for i in range(len(matrixA))]

def matrix_sub(matrixA, matrixB):
    return [[matrixA[i][j] - matrixB[i][j] for j in range(len(matrixA[0]))] for i in range(len(matrixA))]

# Example usage
if __name__ == '__main__':
    # Take 4x4 matrices as input
    print("Enter 4x4 matrix A:")
    matrixA = [[int(input()) for _ in range(4)] for _ in range(4)]
    
    print("Enter 4x4 matrix B:")
    matrixB = [[int(input()) for _ in range(4)] for _ in range(4)]
    
    # Multiply matrices using Strassen's algorithm with step-by-step display
    print("\nStrassen's algorithm step-by-step demonstration:")
    result = strassen(matrixA, matrixB, display_steps=True)
    
    # Print the final result matrix
    print("\nThe final result matrix C (product of matrix A and matrix B):")
    for row in result:
        print(' '.join(map(str, row)))
