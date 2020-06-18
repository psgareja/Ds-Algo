class Node:
    slots='elements','_next'
    def __init__(self,elements,next):
        self.element=element
        self._next=next

    class Node:
        slots='elements','_next'

        def __init__(self,element,next):
            self.element=element
            self._next=next
        def __init__(self):
            self.head=None
            self.size=0

        def __len__(self):
            return self.size
        def is_empty(self):
            return self.size==0

        def push(self,e):
            self.head=self.Node(self,self.head)
            self.size+=1
        def top(self):
            if self.is_empty():
                raise Empty('Stack is empty')
            return self.head.element
        def pop(self):
            if self.is_empty():
                raise Empty('Stack is empty')
            answer=self.head._next
            self.size-=1
            return answer
            

        


