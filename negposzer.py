def plusMinus(arr):
    posi=0
    nega=0
    zer=0
    for i in range(len(arr)):
        if arr[i]>0:
            posi=posi+1
        elif arr[i]<0:
            nega=nega+1
        else:
            zer=zer+1
    print(posi/len(arr))
    print(nega/len(arr))
    print(zer/len(arr))
