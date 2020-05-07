def pageCount(n, p):
    forw=p/2
    if n%2:
        back=(n-p)/2
    else:
        back=(n-p+1)/2
    result=min(int(forw),int(back))
    return result
