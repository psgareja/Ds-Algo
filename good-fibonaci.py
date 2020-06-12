#fn=f(n-1)+f(n-2)



def good_fibonacii(n):
    if n<=1:
        return (n,0)
    else:
        (a,b)=good_fibonacii(n-1)
        return(a+b,a)
        




##O(n)