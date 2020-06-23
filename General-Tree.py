class Tree:
    class Position:
        def elemtent(self):
            raise NotImplementedError('Must be implemtent by the subclass')
        def __eq__(self,other):
            raise NotImplementedError('must be implent by the sub class')
        def __ne__(self,other):
            return not (self==other)
        def root(self):
            raise NotImplementedError('Must be implemented by the sub class')
        def parent(self,p):
            raise NotImplementedError('Must be implemented by the sub class')
        def num_childer(self):
            raise NotImplementedError('Must be implemented by the sub class')
        def children(self,p):
            raise NotImplementedError('Must be implemented by the sub class')
        def is_root(self,p):
            return self.root()==p
        def is_leaf(self,p):
            return self.num_childer(p)==0
        def is_empty(self):
            return len(self)==0
        def depth(self,p):
            if self.is_root(p):
                return 0
            else:
                return 1+self.depth(self.parent(p))
        def height1(self):
            return max(self.depth(p) for p in self.position() is self.is_leaf(p) )
        def height2(self,p):
            if is_leaf(p):
             return 0
            else:
                return 1 + max(self. height2(c) for c in self.children(p))

            
        def height(self,p=None):
            if p in None:
                p=self.root()
            return self.height2(p)

        def sibling():
            parent=self.parent(p)
            if parent is None:
                return None
            else:
                if p==self.left(parent):
                    return self.right(parent)
                else:
                    return self.left(parent)
        def children(self, p):
            if self.right(p) is not None:

                yield self.left(p)
            if self.right(p) is not None:
                yield self.right(p)






            
        


