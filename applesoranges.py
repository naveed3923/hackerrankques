import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    appl_pos=[]
    orange_pos=[]
    ad=0
    od=0
    apc=0
    orc=0
    
    for x in apples:
        ad=x+a
        appl_pos.append(ad)
    for y in oranges:
        od=y+b
        orange_pos.append(od)
    for i in appl_pos:
        if i in range(s,t+1):
            apc=apc+1
    for j in orange_pos:
        if j in range(s,t+1):
            orc=orc+1
    print(apc)
    print(orc)
    


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
