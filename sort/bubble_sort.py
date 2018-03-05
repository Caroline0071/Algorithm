'''
冒泡排序
'''

import random

def bubble_sort(seq):
    count = len(seq)
    for i in range(0, count):
        for j in range(i+1, count):
            if seq[i] > seq[j]:
                seq[i], seq[j] = seq[j], seq[i]
    return seq

def test_bubble_sort():
    seq = [x for x in range(10)]
    seq = random.sample(seq, 10)
    assert(bubble_sort(seq) == sorted(seq))
    print('PASS')

if __name__ == '__main__':
    test_bubble_sort()