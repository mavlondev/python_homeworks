# 1. Create a vector with values ranging from 10 to 49.
# 2. Create a 3x3 matrix with values ranging from 0 to 8.
# 3. Create a 3x3 identity matrix.
# 4. Create a 3x3x3 array with random values.
# 5. Create a 10x10 array with random values and find the minimum and maximum values.
# 6. Create a random vector of size 30 and find the mean value.
# 7. Normalize a 5x5 random matrix.
# 8. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product).
# 9. Create two 3x3 matrices and compute their dot product.  
# 10. Given a 4x4 matrix, find its transpose.  
# 11. Create a 3x3 matrix and calculate its determinant.  
# 12. Create two matrices \( A \) (3x4) and \( B \) (4x3), and compute the matrix product \( A \cdot B \).  
# 13. Create a 3x3 random matrix and a 3-element column vector. Compute the matrix-vector product.  
# 14. Solve the linear system \( Ax = b \) where \( A \) is a 3x3 matrix, and \( b \) is a 3x1 column vector.  
# 15. Given a 5x5 matrix, find the row-wise and column-wise sums.

#task 1
import numpy as np
vector = np.arange(10, 50)

#task 2
matrix_3x3 = np.arange(9).reshape(3, 3)

#task 3
identity_matrix = np.eye(3)

#task 4
random_array_3x3x3 = np.random.rand(3, 3, 3)

#task 5
random_array_10x10 = np.random.rand(10, 10)

min_value = np.min(random_array_10x10)
max_value = np.max(random_array_10x10)

#task 6
random_vector_30 = np.random.rand(30)
mean_value = np.mean(random_vector_30)

#task 7
random_matrix_5x5 = np.random.rand(5, 5)
normalized_matrix = (random_matrix_5x5 - np.min(random_matrix_5x5)) / (np.max(random_matrix_5x5) - np.min(random_matrix_5x5))

#task 8
matrix_5x3 = np.random.rand(5, 3)
matrix_3x2 = np.random.rand(3, 2)
product_5x2 = np.dot(matrix_5x3, matrix_3x2)

#task 9
matrix_A = np.random.rand(3, 3)
matrix_B = np.random.rand(3, 3)
dot_product = np.dot(matrix_A, matrix_B)

#task 10
matrix_4x4 = np.random.rand(4, 4)
transpose_matrix = np.transpose(matrix_4x4)

#task 11
matrix_3x3_for_determinant = np.random.rand(3, 3)
determinant_value = np.linalg.det(matrix_3x3_for_determinant)

#task 12
matrix_A_3x4 = np.random.rand(3, 4)
matrix_B_4x3 = np.random.rand(4, 3)
matrix_product_AB = np.dot(matrix_A_3x4, matrix_B_4x3)

#task 13
matrix_3x3_random = np.random.rand(3, 3)
column_vector_3 = np.random.rand(3, 1)
matrix_vector_product = np.dot(matrix_3x3_random, column_vector_3)

#task 14
matrix_A_3x3 = np.random.rand(3, 3)
b_3x1 = np.random.rand(3, 1)
solution_x = np.linalg.solve(matrix_A_3x3, b_3x1)

#task 15
matrix_5x5 = np.random.rand(5, 5)
row_sums = np.sum(matrix_5x5, axis=1)
column_sums = np.sum(matrix_5x5, axis=0)