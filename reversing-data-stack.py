def reverse_file(filename):
    S=ArrayStack()
    origin=open(filename)
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()

    outpust=open(filename,'w')
    while not S.is_empty():
        output.write(S.pop()+'\')
    output.close()
    