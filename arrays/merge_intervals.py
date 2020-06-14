# Merge overlapping intervals

'''Merge overlapping intervals
1. Time O(n)
2. Space O(n)
'''

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
   merged = []
   intervals.sort(key=lambda x:x[0])
      
   for interval in intervals:
        if merged and interval[0] <= merged[-1][1]:
            merged[-1][1] = max(interval[1], merged[-1][1])
        else:
            merged.append(interval)

    return merged
