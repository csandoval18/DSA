from typing import List

# Matrix Multiplication
#  A        B
# [1,2] *  [2]
# [3,1]    [3]
#  2*2     2*1

# These two matrices are able to be multiplied because they share a 2 in their dimensions
# (2*2) * (2*1) = 2 * (2*2) * 1 = 2 * 1
#                  remove ^


def matrix_chain_multiplication(matrix: List):