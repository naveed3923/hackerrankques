def birthday(s, d, m):
    count=0
    for i in range((len(s))-(m-1)):
        a=s[i:i+m]
        if sum(a)==d:
            count=count+1
    return count
