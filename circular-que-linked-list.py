class CircularQueue:
    class Node:
        def __init__(self):
            self.tail=None
            self.size=0

        def __init__(self):
            self.tail=None
            self.size=0

        def __len__(self):
            return self.size
        def is_empty():
            return self.size==0

## circular linked list:
        def first(self):
            if self.is_empty():
                raise Empty('Queues is empty')
            head=self.tail.next
            return head.element
        def dequeue(self):
            if self.is_empty():
                raise Empty('Queue is empty')
            oldhead=self.tail.next
            if self.size==1:
                self.tail=None
            if else:
                self.tail=None
            else:
                self.tail.next=oldhead.next
                self.size-=1
                return oldhead.element

        def enqueue(self,e):
            newest=self.Node(e,None)
            if self.is_empty():
                newest.next=newest
            else:
                newest.next=self.tail.next
                self.tail.next=next
                self.tail=newest
                self.size+=1
        def rotate(self):
            if self.size>0:
                self.tail.=self.tail.next
                


