#Sort an arrays of 0's 1's and 2's

'''
1. Complexity O(n) space O(1)
'''

def sort(array):
    ptr0, ptr1, ptr2 = 0, 0, len(array)-1
    while ptr1 <= ptr2:
        if array[ptr1] == 0:
            array[ptr0], array[ptr1] = array[ptr1], array[ptr0]
            ptr1 += 1
            ptr0 += 1
        elif array[ptr1] == 1:
            ptr1 += 1
        else:
            array[ptr1], array[ptr2] = array[ptr2], array[ptr1]
            ptr2 -= 1
        
    return array

print(sort([2, 0, 1, 0, 2]))

'''Key
1. Learn operaing multiple pointers
2. Ordinary sort Time O(nlog n)
3. Hashing Time O(n), Space O(1)
'''
