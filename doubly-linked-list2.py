class PostionalList(_DoublyLinkedListBase):
    class Position:
        def __init__(self,container,node):
            self.container=container
            self.node=node

        def elemtn(self):
            return self.node.elemtn
        def __eq__(self,other):
            return type(other) is type(self) and other.node.is self.node

        def __ne__(seld,other):
            return not (self==other)
        def validate(self,p):
            if not isinstance(p,self.Position):
                raise TypeError('p must be in proper postion')
            if p.container is not self:
                raise ValueError('p does not belog to container')
            if p.node.next is None:
                raise ValueError('p is not longer valid ')
            return p.node
        def make_position(self,node):
            if node is self.header or node is self.trailer:
                return None
            else:
                return self.Position(self,node)

        def first(self):
            return self.make_position(self.header.next)

        def last(self):
            return self.make_position(self.trailer.prev)
        def after(self,p):
            node=self.validate(p)
            return self.make_position(node.next)
        def __iter__(self):
            cursor=self.first()

            while cursor is not None:
                yield cursor.element()
                cursor=self.after(cursor)
        def insert_between(self,e,pre,suc):
            node=super.insert_between(e,pre,suc)
            return self.make_position(node)
        def add_first(self,e):
            return self.insert between(e, self.header, self.header.next)
        def add_last(self,e):
            return self.insert_between(e, self. trailer. prev, self. trailer)
        def add_before(self,p,e):
            original=self.validate(p)
            return self.insert_between(e, original. prev, original)
        def delete(self,p,e):
            original=self.validate(p)
            return self.delete.node(original)
        def replace(self,p,e):
            original=self.validate(p)
            old_value=original.elemtn
            original.elemtn=e
            return old_value
        def insertion_sort(L):
            if len(L)>1:
                marker=L.first()
                while =L.first()
                pivot=L.after(marker)
                value=pivot.elemtn()
                if value>marker.elemtn():
                    marker=pivot
                else:
                    walk=marker
                    while walk!=L.first() and L.before(walk).elemtn()>value:
                        L.delete(pivot)
                        L.add_before(walk,value)



        
        
        class FavoritesList:
            class Item:
                __slots__='value','count'
                def __init__(self,e):
                    self.value=e
                    self.count=0

                def find_postion(self,e):
                    walk=self.data.first()
                    while walk is not None and walk.element(). value != e:
                        walk=self.data.after(walk)
                    return walk

                def move_up(self,p):
                    if p !=self.data.first():
                        cnt=p.elemtn().count()
                        walk=self.data.before(p)
                        if cnt>walk.elemtn().count:
                            while (walk != self. data.first( ) and
                                        cnt > self. data.before(walk).element(). count):
                                    walk = self. data.before(walk)
                            self. data.add before(walk, self. data.delete(p))
                def init (self):
”””Create an empty list of favorites.”””
self. data = PositionalList( ) # will be list of Item instances
def len (self):
”””Return number of entries on favorites list.””” return len(self. data)
def is empty(self):
”””Return True if list is empty.””” return len(self. data) == 0
def access(self, e):
”””Access element e, thereby increasing its access count.”””
             p = self. find position(e) if p is None:
p = self. data.add last(self. Item(e)) p.element(). count += 1
self. move up(p)
# try to locate existing element
# if new, place at end
# always increment count # consider moving forward
        def remove(self, e):
”””Remove element e from the list of favorites.”””
p = self. find position(e) # try to locate existing element if p is not None:
self. data.delete(p) # delete, if found
def top(self, k):
”””Generate sequence of top k elements in terms of access count.””” if not 1 <= k <= len(self):
raise ValueError( Illegal value for k ) walk = self. data.first()
for j in range(k):
item = walk.element( ) # element of list is Item yield item. value # report user’s element walk = self. data.after(walk)


