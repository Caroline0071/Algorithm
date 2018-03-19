'''
read(),readline(),readlines()
'''

import readline

def read_file(filename):
    for line in filename.readlines():




if __name__ == '__main__':
    filename = open('/Users/liyajuan02/Downloads/logcat.log', 'r')
    read_file(filename)