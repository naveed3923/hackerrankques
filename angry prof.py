#!/usr/bin/env python
# coding: utf-8

# In[1]:


# ANGRY PROFESSOR
# 'k' is threshold number of students so that class isn't cancelled
# a is the array mentioning arrival time of each students
# a[i]<=0 (on time), a[i]>0 (late arrival)

def AngryProfessor(k,a):
    p=0
    for i in a:
        if i<=0:
            p=p+1
    if p>=k:
        result='NO'
    else:
        result='YES'
    return result

print(AngryProfessor(3,[-1,-2,1,3,-1]))
        


# In[ ]:




