'''
使用list实现栈
'''

class Stack(list):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, elememt):
        self.items.append(elememt)

    def pop(self):
        if not self.isEmpty():
            self.items.pop()
        else:
            raise Exception("Stack is empty")

    def peek(self):
        return self.items[-1]

    def size(self):
        return (len(self.items))

def test_stack():
    stack_a = Stack()
    stack_a.push(1)
    stack_a.push(2)
    stack_a.push(3)
#    print(stack_a)
    print(stack_a.size())
    print(stack_a.peek())
    print(stack_a.pop())
    print(stack_a.peek())

if __name__ == '__main__':
    test_stack()
