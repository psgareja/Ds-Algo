def binary_sum(s,start,stop):
    if start>=stop:
        return 0
    elif start==stop-1:
        return S[start]
    else:
        mid=(start+stop)//2
        return binary_sum(S,start,mid)+binary_sum(S,mid,stop)



#Summing the elements of a sequence using binary recursion.
#recursion 1+logn 
#sum log(n)
#binary summ o(n)
#total function call 2n-1