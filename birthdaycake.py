def birthdayCakeCandles(ar):
    count=0
    a=max(ar)
    for i in ar:
        if i==a:
            count=count+1
    return count
