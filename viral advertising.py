#!/usr/bin/env python
# coding: utf-8

# In[8]:


# n denotes no of days

def viral_advertising(n):
    shared=5
    liked_list=list()
    for i in range(1,n+1):
        liked=shared//2
        liked_list.append(liked)
        shared=3*liked
    return sum(liked_list)

        
print(viral_advertising(5))
        
        
    


# In[3]:


3//2


# In[ ]:




