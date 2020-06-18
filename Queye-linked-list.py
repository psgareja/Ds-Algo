class LinkedQueue:
    class Node:
        def __init__(self):
            self.head=None
            self.tail=None
            self.size=0

        def __len__(self):
            return self.size
        def is_empty(self):
            return self.size==0
        def first(self):
            if self.is_empty():
                raise Empty("Queue is empty")
            return self.head.element
        def dequeue(self):
            if self.is_empty():
                raise Empty('Queue is empty ')
            answer=self.head.element
            self.head=self.head.next
            self.size-=1
            if self.is_empty():
                self.til=None
            return answer
        def enqueue(self,e):
            newest=self.Node(e,None)
            if self.is_empty():
                self.head=newest
            else:
                self.tail.next=newest
                self.tail=newest
                self.size+=1
                


      
