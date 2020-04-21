#!/usr/bin/env python
# coding: utf-8

# In[50]:


def timeConversion(s):
    time=s.split(':')
    if s[-2:]=='PM':
        if time[0]!='12':
            time[0]=str(int(time[0])+12)
    else:
        if time[0]=='12':
            time[0]='00'
    final=':'.join(time)
    finale=str(final[:-2])
    return finale


# In[ ]:





# In[ ]:




