class Stack():
    def __init__(self, length):
        self.pointer = 0
        self.length = length
        self.CreateStack()

    def CreateStack(self):
        self.array = [None] * self.length

    def Push(self, value):
        if self.pointer == self.length:
            return print('stack full')
        self.array[self.pointer] = value
        self.pointer += 1

    def Pop(self):
        if self.pointer == 0:
            return print('stack empty')
        temp = self.array[self.pointer - 1]
        self.array[self.pointer - 1] = None
        self.pointer -= 1
        return temp

    def Display(self):
        print(self.array)


stack1 = Stack(10)
stack1.Pop()
stack1.Display()
for i in range(11):
    stack1.Push(2)
    stack1.Display()

print(stack1.Pop())
