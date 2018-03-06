'''
归并排序
'''

import random

def merge_sort(seq):
    if len(seq) < 2:
        return seq
    left = None
    right = None
    mid = len(seq) // 2
    if seq[:mid]:
        left = merge_sort(seq[:mid])  #left是有序的
    if seq[mid:]:
        right = merge_sort(seq[mid:]) #right是有序的
    return merge_n(left, right)


def merge_n(left, right):  #合并两个有序数列
    if not left or not right:
        return left or right
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            print(result)
            j += 1
    result += left[i:]
    result += right[j:]
#    print(result)
    return result

def merge_2n(left, right):
    if not left or not right:
        return left or right
    result = []
    while left and right:
        if left[-1] >= right[-1]:
            result.append(left.pop())
        else:
            result.append(right.pop())
    result.reverse()
    return (left or right) + result


def test_merge_sort():
    seq = [x for x in range(10)]
    seq = random.sample(seq, 10)
#    print(seq)
    assert(merge_sort(seq) == sorted(seq))
    print('PASS')

if __name__ == '__main__':
    test_merge_sort()