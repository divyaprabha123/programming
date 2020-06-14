import heapq

'''Sorting k arrays
1. Use heap time O(n) space O(n)
'''

def merge_arrays(arrays):
    heap = [(lst[0], i,0) for i, lst in enumerate(arrays) if lst]
    heapq.heapify(heap)
    merge = []
    while heap:
        min_num, lst_index, ele_index = heapq.heappop(heap)
        merge.append(min_num)
        if len(arrays[lst_index]) > ele_index+1:
            heapq.heappush(heap, (arrays[lst_index][ele_index+1], lst_index,\
                                  ele_index + 1))

    return merge

print(merge_arrays([[1,2,4], [3,6,5]]))
            
'''keys
1. Ordinary sort O(nlog n)
2. Learn index out of error when using two pointers approach
'''
