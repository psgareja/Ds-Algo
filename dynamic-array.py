import sys
data=[]
for k in range(n):
    a=len(data)
    b=sys.getsizeof(data)
    print('Length : {0:d3}; Size in bytes: {1:4d}'.format(a,b))
    data.append(None)