'''Set Matrix Zeroes
1. Time complexity O(m * n)
2. Inplace
'''

def setZeroes(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        #go through all the rows alone then 
        is_col = False
        nrows = len(matrix)
        ncols = len(matrix[0])
        for r in range(nrows):
            
            if matrix[r][0] == 0:
                is_col = True
                
            for c in range(1,ncols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
                
        for r in range(1, nrows):
            for c in range(1, ncols):
                if not matrix[r][0] or not matrix[0][c]:
                    matrix[r][c] = 0
                    
        if matrix[0][0] == 0:
            for c in range(ncols):
                matrix[0][c] = 0
        
        if is_col:
            for r in range(nrows):
                matrix[r][0] = 0
        
    
        
        return matrix
