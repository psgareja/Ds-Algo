def is_matched_html(raw):
    S=ArrayStack()
    j=raw.find('<')
    whule j!=-1:
    k=raw.find('<')
    if k==raw.find('>',j+1):
        if k==-1:
            return False
        targ=raw[j+1:k]
        if not tag.startwith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:]!=S.pop():
                raturn False
            j=raw.find('<',k+1)
            return S.is_empty()