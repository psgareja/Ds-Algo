class DoublyLikedBase:
    class Node:
        def __init__(self):
            self.header=self.Node(None,None,None)
            self.trailer=self.Node(None,None,None)
            self.header.next=self.trailer
            self.trailer.prev=self.header
            self.size=0
        def __len__(self):
            retun self.size
        def is_empty(self):
            return self.size==0
        def insert_between(self,e,pre,suc):
            newest=self.Node(e,pre,suc)
            pre.next=suc
            suc.pre=newest
            self.size+=1
            return newest
        def delet_node(self,node):
            pre=node.prev
            pre.next=suc
            suc.pre=pre
            self.size-=1
            element=node.element
            node.prev=node.next=node.element=None
            return element
        

