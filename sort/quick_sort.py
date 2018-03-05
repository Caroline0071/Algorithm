'''
快速排序：分为递归和非递归
递归：选择pivot，即中轴元素，按照中轴元素将数组分为两个，左边是小于等于pivot的元素，右边是大于pivot的元素
非递归：
'''

import random

def quick_sort(seq):
    if len(seq) < 2:
        return seq

    left = 0
    right = len(seq)
    mid = (left+right) // 2

    pivot = seq[mid]
    seq = seq[:mid] + seq[mid+1:]

    lo = [x for x in seq if x <= pivot]
    hi = [x for x in seq if x > pivot]

    return quick_sort(lo) + [pivot] + quick_sort(hi)


def quick_sort2(seq, start, end):
    if start < end:
        pivot = partition(seq, start, end)
        quick_sort2(seq, start, pivot)
        quick_sort2(seq, pivot+1, end)
    return seq

def partition(seq, start, end):
    pivot = seq[start]
    while start < end:
        while start < end and seq[end] >= pivot:
            end -= 1
        while start < end and seq[end] < pivot:
            seq[start] = seq[end]
            start += 1
            seq[end] = seq[start]
    seq[start] = pivot
    return start


def test_quick_sort():
    seq = [x for x in range(10)]
#    print(seq)
    seq = random.sample(seq,10)
#    print(seq)
    assert(quick_sort(seq) == sorted(seq))
    print("PASS")
    assert (quick_sort2(seq, 0, len(seq)-1) == sorted(seq))
    print("PASS")

if __name__ == "__main__":
    test_quick_sort()

