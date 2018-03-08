'''
Two stack to implement queue
在一个栈顶进行push操作、在一个栈顶进入pop操作
'''

class Queue(object):
    def __init__(self):
        self.inStack = []
        self.outStack = []

    def enqueue(self, element):
        self.inStack.append(element)

    def dequeue(self):
        if self.outStack:    # 出栈不为空
            return self.outStack.pop()
        while self.inStack: # 出栈为空，将inStack进行pop操作后，对outStack进行push操作
            self.outStack.append(self.inStack.pop())
        if not self.outStack:
            raise Exception('Queue Empty')
        return self.outStack.pop()

    def size(self):
        return len(self.inStack) + len(self.outStack)

    def peek(self):
        if self.outStack:  #outStack不为空
            return self.outStack[-1]  #返回outStack的栈顶元素，即为list的最后一个元素
        while self.inStack:  #outStack为空，出inStack入outStack
            return self.outStack.append(self.inStack.pop())
        print(self.outStack)
        if self.outStack:
            return self.outStack[-1]
        else:
            return None


def test_queue():
    queue1 = Queue()
    queue1.enqueue(4)
    queue1.enqueue(3)
    queue1.enqueue(1)
    print(queue1.size())
    print(queue1.peek())  #栈顶返回为空  ???原因排查
    print(queue1.dequeue())
    print(queue1.peek())  #栈顶返回为空

if __name__ == '__main__':
    test_queue()




