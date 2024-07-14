import numpy as np

def input_matrix(m, n):
    print('Enter matrix:')
    for i in range(n):
        for j in range(n):
            m[i][j] = int(input(f'Enter element [{i+1},{j+1}]: '))
    print()

def print_matrix(m, n):
    for i in range(n):
        for j in range(n):
            print(m[i][j], end=' ')
        print()
    print()

def strassen(a, b):
    n = len(a)
    if n == 1:
        return a * b
    
    c = np.zeros((n, n), dtype=np.int64)
    k = n // 2

    a11 = a[:k, :k]
    a12 = a[:k, k:]
    a21 = a[k:, :k]
    a22 = a[k:, k:]

    b11 = b[:k, :k]
    b12 = b[:k, k:]
    b21 = b[k:, :k]
    b22 = b[k:, k:]

    P = strassen(a11 + a22, b11 + b22)
    Q = strassen(a21 + a22, b11)
    R = strassen(a11, b12 - b22)
    S = strassen(a22, b21 - b11)
    T = strassen(a11 + a12, b22)
    U = strassen(a11 - a21, b11 + b12)
    V = strassen(a12 - a22, b21 + b22)

    c11 = P + S - T + V
    c12 = R + T
    c21 = Q + S
    c22 = P + R - Q - U

    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
    return c

if __name__ == '__main__':
    print("Strassen's Matrix Multiplication Algorithm\n" +
          "Enter a number with the power of 2.")
    n = int(input('Enter size of matrix: '))

    a = np.zeros((n, n), dtype=np.int64)
    b = np.zeros((n, n), dtype=np.int64)

    input_matrix(a, n)
    print('Matrix A:')
    print_matrix(a, n)

    input_matrix(b, n)
    print('Matrix B:')
    print_matrix(b, n)

    c = strassen(a, b)
    print('Multiplication result:')
    print_matrix(c, n)
