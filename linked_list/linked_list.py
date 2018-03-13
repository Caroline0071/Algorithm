'''
Implement Node
'''

class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

    def getItem(self):
        return self.item

    def getNext(self):
        return self.next

    def setItem(self, item):
        self.item = item

    def setNext(self, next):
        self.next = next

if __name__ == '__main__':
    s = Node(4)
    s.setItem(1)
    s.setItem(2)
    s.setItem(3)
    value = s.getItem()
    print(s)
    print(value)