def kangaroo(x1, v1, x2, v2):
    jump=0
    jum=0
    if x1==x2 and v1==v2:
        return('YES')
    elif (x1!=x2 and v1==v2) or (x1==x2 and v1!=v2):
        return('NO')
    elif (v2!=v1 and (x1-x2)%(v2-v1)==0 and (x1-x2)/(v2-v1)>=0):
        return('YES')
    else:
        return('NO')
