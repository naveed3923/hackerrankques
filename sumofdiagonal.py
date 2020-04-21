def diagonalDifference(arr):
    a=0
    b=0
    for i in range(len(arr)):
        a=arr[i][i]+a
        b=arr[i][len(arr)-i-1]+b
    result=abs(a-b)
    return result
