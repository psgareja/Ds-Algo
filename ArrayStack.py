class ArrayStack:
    def __init__(self):
        self.data=[]
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        if self.data==0:
            print('No value in stack')
    def push(self,e):
        self.data.append(e)
    def top(self):
        if self.is_empty():
            raise Empty('Stack has no value')
        return self.data[-1]
    def pop(self):
        if self.is_empty():
            raise Empty('Stack has no value')
        return self.data.pop()

