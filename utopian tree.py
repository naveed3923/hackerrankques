#!/usr/bin/env python
# coding: utf-8

# In[4]:


#evaluating height of tree after every summer and spring season (after a given no of cycles)

def utopian_tree(n):
    hyt_list=list()
    hyt=1
    hyt_list.append(hyt)
    for i in range(1,n+1):
        if i%2!=0:
            hyt=2*hyt
        else:
            hyt=hyt+1
        hyt_list.append(hyt)
    return hyt_list[n]

print(utopian_tree(5))
    


# In[ ]:




