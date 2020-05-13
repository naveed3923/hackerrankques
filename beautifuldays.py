#!/usr/bin/env python
# coding: utf-8

# In[32]:


# BEAUTIFUL DAYS
# i and j is the range of dates (j inclusive)
# k is the divisor for the absolute difference of number and its reverse (in the range of i and j)

def beautifulDays(i, j, k):
    total=0
    for n in range(i,j+1):
        new=''
        ab=[y for y in str(n)]
        rev=[z for z in reversed(ab)]
        for p in rev:
            new=new+p
        new=int(new)
        diff=abs(new-n)
        result=diff%k
        if result==0:
            total=total+1
    return total

print(beautifulDays(20,23,6))





# In[ ]:




