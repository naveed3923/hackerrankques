def divisibleSumPairs(n, k, ar):
    n=len(ar)
    count=0
    for i in range(n):
        for j in range(n):
            if i!=j:
                if i<j:
                    if(ar[i]+ar[j])%k==0:
                        count=count+1
    return count
