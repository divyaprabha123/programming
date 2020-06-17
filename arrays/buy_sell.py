'''Stock buy and cell
1. Greedy search
'''

def maxProfit(self, prices: List[int]) -> int:
    length = len(prices)
    if length <= 1:
        return 0
    max_profit = 0
    buy = prices[0]

    for i in range(1, length):            
        profit = prices[i] - buy
        max_profit = max(max_profit, profit)
        if buy > prices[i]:
            buy = prices[i]

    return max(max_profit, 0)

'''
1. Time Complexity : O(n)
2. Space Complexity : O(1)
'''