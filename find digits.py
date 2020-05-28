#!/usr/bin/env python
# coding: utf-8

# In[9]:


#finding digits (given a number n, check if n is divisible by its constituent digits. count the no of such divisors)

def find_digits(n):
    divisors=0
    n_str=[x for x in str(n)]
    indiv=[int(i) for i in n_str]
    for p in indiv:
        if p!=0 and n%p==0:
            divisors=divisors+1
    return divisors

print(find_digits(1012))
    


# In[ ]:




