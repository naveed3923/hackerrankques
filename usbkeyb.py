def getMoneySpent(keyboards, drives, b):
    c=0
    final=list()
    for i in keyboards:
        for j in drives:
            c=i+j
            if c<=b:
                final.append(c)
            else:
                final.append(0)
    result=max(final)
    nom=0
    if result==0:
        nom=-1
    else:
        nom=result
    return(nom)
