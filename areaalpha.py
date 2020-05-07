def designerPdfViewer(h, word):
    result=0
    hmax=0
    fresh=dict()
    alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(len(alpha)):
        if alpha[i] not in fresh:                         
            fresh[alpha[i]]=h[i]
    final=list()
    for i in word:
        final.append(fresh[i])
    hmax=max(final)
    result=hmax*len(final)
    return result
