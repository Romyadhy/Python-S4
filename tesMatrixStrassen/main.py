def strassen(matrixA, matrixB):
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
    
    # Calculate the 7 products recursively
    M1 = strassen(matrix_sub(A12, A22), matrix_add(B21, B22))
    M2 = strassen(matrix_add(A11, A22), matrix_add(B11, B22))
    M3 = strassen(matrix_sub(A11, A21), matrix_add(B11, B12))
    M4 = strassen(matrix_add(A11, A12), B22)
    M5 = strassen(A11, matrix_sub(B12, B22))
    M6 = strassen(A22, matrix_sub(B21, B11))
    M7 = strassen(matrix_add(A21, A22), B11)
    
    # Calculate the 4 quadrants of the final matrix
    C11 = matrix_add(matrix_sub(matrix_add(M1, M2), M4), M6)
    C12 = matrix_add(M4, M5)
    C21 = matrix_add(M6, M7)
    C22 = matrix_sub(matrix_add(M2, M5), matrix_add(M3, M7))
    
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
    
    # Multiply matrices using Strassen's algorithm
    result = strassen(matrixA, matrixB)
    
    # Print the result
    print("The product of matrix A and matrix B is:")
    for row in result:
        print(' '.join(map(str, row)))
