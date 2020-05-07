def hurdleRace(k, height):
    a=max(height)
    final=0
    if k>=a:
        final=0
    else:
        final=a-k
    return final
