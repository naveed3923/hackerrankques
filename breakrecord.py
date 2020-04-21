def breakingRecords(scores):
    maxm=scores[0]
    minm=scores[0]
    min_c=0
    max_c=0
    for i in range(1,len(scores)):
        if scores[i]>maxm or scores[i]<minm:
            if scores[i]>maxm:
                maxm=scores[i]
                max_c=max_c+1
            if scores[i]<minm:
                minm=scores[i]
                min_c=min_c+1
        else:
            maxm=maxm
            minm=minm
            max_c=max_c
            min_c=min_c
    return(max_c,min_c)
