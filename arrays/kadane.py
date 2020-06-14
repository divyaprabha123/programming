#Kadane's algorithm

'''Maximum sum sub array
1. Time Complexity O(n) Space O(n)
'''

def max_sum(nums):
    max_so_far = nums[0]
    max_ending_here = nums[0]        
    for i in range(1,len(nums)):
        max_ending_here = max(max_ending_here+nums[i],nums[i])
        max_so_far = max(max_so_far,max_ending_here)
    return max_so_far

print(max_sum([-2, -3, 4, -1, -2, 1, 5, -3]))


