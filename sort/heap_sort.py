'''
Heap Sort
Build Heap
Adjust Heap
'''

def adjust_heap(seq, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size//2:
        if lchild < size and seq[lchild] > seq[max]:
            max = lchild
        if rchild < size and seq[rchild] > seq[max]:
            max = rchild
        if max != i:
            seq[max], seq[i] = seq[i], seq[max]
            adjust_heap(seq, max, size)


def build_heap(seq, size):
    for i in range(0,(size//2))[::-1]:
        adjust_heap(seq, i, size)


def heap_sort(seq):
    size = len(seq)
    build_heap(seq, size)
    for i in range(0, size)[::-1]:
        seq[0], seq[i] = seq[i], seq[0]
        adjust_heap(seq, 0, i)
