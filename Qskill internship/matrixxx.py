import numpy as np

# Input matrices
print("Enter elements for Matrix A (2x2):")
A = np.array([[int(input()), int(input())],
              [int(input()), int(input())]])

print("\nEnter elements for Matrix B (2x2):")
B = np.array([[int(input()), int(input())],
              [int(input()), int(input())]])

print("\nMatrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Operations
print("\nAddition of A and B:")
print(A + B)

print("\nSubtraction of A and B:")
print(A - B)

print("\nMultiplication of A and B:")
print(np.dot(A, B))

print("\nTranspose of Matrix A:")
print(A.T)

print("\nDeterminant of Matrix A:")
print(np.linalg.det(A))
