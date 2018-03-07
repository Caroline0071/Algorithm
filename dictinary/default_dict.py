'''
defaultdict usage
'''

from collections import defaultdict

def defaultdict_test():
    pairs = {('a',1), ('b',2), ('c',3)}
    print(pairs)
    d1 = {}
    for key, value in pairs:
        if key not in d1:
            d1[key] = []  #key不在添加key
        d1[key].append(value)  #key在，添加值
    print(d1)

    d2 = defaultdict(list)
    for key, value in pairs:
        d2[key].append(value)  #d2是list，
        print(d2)
    print(d2)

if __name__ == '__main__':
    defaultdict_test()