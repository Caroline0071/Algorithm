'''
Counting frequency items
统计前n个words的频次
多次运行有失败
'''

from collections import Counter

def find_top_n_recurring_words(seq, n):
    dcounter = Counter() #创建字典
    for word in seq.split():
        dcounter[word] += 1
    return dcounter.most_common(n)

def test_find_top_n_words(module_name='this module'):
    seq = 'buffy angel monster xander a willow gg buffy the monster super buffy angel'
    n = 3
    d1 = find_top_n_recurring_words(seq, n)
    print(d1)
    assert(find_top_n_recurring_words(seq, n) == [('buffy',3),('angel',2),('monster',2)])
    s = 'Test in {name} have {con}'
    print(s.format(name=module_name, con='PASS'))

if __name__ == '__main__':
    test_find_top_n_words()