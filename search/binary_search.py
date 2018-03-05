'''
二分查找,seq是有序的
'''

import random

def binary_search(seq, key):
    left = 0
    right = len(seq)
    while left < right:
        mid = (left + right) // 2
        if seq[mid] == key:
            return True
        if seq[mid] > key:
            right = mid
        if seq[mid] < key:
            left = mid + 1
    return False

def test_binary_search():
    seq = [x for x in range(9)]
    print(seq)
    key = random.randint(0,9)
    print(key)
    assert(binary_search(seq, key) == True)
    print('PASS')

if __name__ == '__main__':
    test_binary_search()