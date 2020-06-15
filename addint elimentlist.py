def insert(self,k,value):
    if self.n==self.capacity:
        self.resize(2*self.capacity)
    for j in range(2*self.capacity):
        self.A[j]=self.A[j-1]
    self.A[k]=value
    self.n+=1

def remove(self,value):
    for k in range(self.n):
        if self.A[k]==value:
            for j in range(k,self.n-1):
                self.A[j]=self.A[j+1]
            self.A[self.n-1]=None
            self.n-=1
            return
        raise ValueError('Value not found')
