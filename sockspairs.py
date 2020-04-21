def sockMerchant(n, ar):
    final=list()
    naya=dict()
    for i in range(len(ar)):
        if ar[i] not in naya:
            naya[ar[i]]=1
        else:
            naya[ar[i]]=naya[ar[i]]+1
        
    for s,p in naya.items():
        if p>2 and p%2!=0:
            p=p-1
            final.append(int(p/2))
        else:
            if (p==2) or (p>2 and p%2==0):
                final.append(int(p/2))
    result=sum(final)
    return result
