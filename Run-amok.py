def unique(S,start,end):
    if stop-start<1:
        return True
    elif not unique(S,start,stop):
        return False
    elif not unique(S,start+1,stop):
        return False
    else:
        return S[start]!=S[stop-1]
        


