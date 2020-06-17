'''Pascal's Triangle
1. Use Dynamic programing
'''

def generate(self, numRows: int) -> List[List[int]]:
    if numRows < 1:
        return []
    lists = [[1]*(i+1) for i in range(numRows)]
    for i in range(numRows):
        for j in range(1, i):
            lists[i][j] = lists[i-1][j-1]+lists[i-1][j]
    return lists

'''
1. Time Complexity : O(n^2)
2. Space Complexity : O(n^2)
'''