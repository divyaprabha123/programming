'''
Matrix Rotate 
1. Inplace
'''

#Solution 1 
#rotate colockwise
#then take transpose

def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    nrows = len(matrix)
    ncols = len(matrix[0])
    for i in range(0, nrows//2):
        for j in range(0, ncols):
            matrix[i][j], matrix[nrows-1-i][j]  = matrix[nrows-1-i][j], matrix[i][j]

    for i in range(0, nrows):
        for j in range(0, i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
#Solution 2 - Pythonic 

def rotate_2(matrix):
    matrix = [[row[i] for row in matrix[::-1]] for i in range(len(matrix))]