'''
setdefault() usage in dictionary
'''

def usual_dict(dict_data):
    newdata = {}
    for k, v in dict_data:
        if k in newdata:
            newdata[k].append(v)  #key在newdata，添加value
        else:
            newdata[k] = v
    return newdata

def set_default_dict(dict_data):
    newdata = {}
    for k, v in dict_data:
        newdata.setdefault(k, []).append(v)

    return newdata
def test_setdict(module_name='This module'):
    dict_data = (('key1', 'value1'),
                 ('key2', 'value2'),
                 ('key3', 'value3'))
    print(usual_dict(dict_data))
    print(set_default_dict(dict_data))

    s = 'Test in {name} have {con}!'
    print(s.format(name=module_name, con='PASS'))

if __name__ == '__main__':
    test_setdict()
