NOTE: 'INPUT VALUES NOT PROVIDED....see in question'

def getTotalX(a, b):
    count=0
    for i in range(1,101):
        if all(i%x==0 for x in a) and all(x%i==0 for x in b):
            count=count+1
    return count
