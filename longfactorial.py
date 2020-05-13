#!/usr/bin/env python
# coding: utf-8

# In[6]:


# used a recursive function to calculate factorial

def extraLongfactorials(n):
    result=0
    if n>1:
        result=n*extraLongfactorials(n-1)
    else:
        result=1
    return result
print(extraLongfactorials(20))


# In[ ]:




