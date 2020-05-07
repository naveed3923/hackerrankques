import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    A=abs(int(x)-int(z))
    B=abs(int(y)-int(z))
    winner=''
    if A<B:
        winner='Cat A'
    elif B<A:
        winner='Cat B'
    else:
        winner='Mouse C'
    
    return winner
