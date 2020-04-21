def miniMaxSum(arr):
    res=sum(arr)
    a=min(arr)
    b=max(arr)
    mini=res-b
    maxm=res-a
    print(mini,maxm)
