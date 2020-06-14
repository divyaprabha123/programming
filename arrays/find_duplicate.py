#Find duplicate in an array of n integers

'''
1. There is only one duplicate number but it can be repeted n times
2. Complete in O(n) time complexity
'''

def find_duplicate(array):
    #Using hare and tortoise method
    #define pointers
    # Time : O(n) Space : O(1)
    tortoise = array[0]
    hare = array[0]

    while True:
        tortoise = array[tortoise]
        hare = array[array[hare]]
        if tortoise == hare:
            break

    ptr1 = array[0]
    ptr2 = tortoise

    while ptr1!=ptr2:
        ptr1 = array[ptr1]
        ptr2 = array[ptr2]

    return ptr1

'''
Other ways and shortcomings
1. Sorting Time : O(nlogn), Space: O(n)
2. Hashing Time : O(n), Space: O(n)
3. Binary search : O(log n) but duplicated number
cannot be repeated more than twice
'''

print(find_duplicate([2,3,3,1,4]))
