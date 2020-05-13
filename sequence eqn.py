#!/usr/bin/env python
# coding: utf-8

# # SEQUENCE EQUATION

# In[49]:


p=[2, 5, 11, 10, 1, 14, 7, 3, 16, 9, 8, 6, 18, 12, 15, 17, 13, 4]
n=len(p)
index_list=list()
for x in range(1,n+1):
    a=p.index(x)
    index_list.append(a)



final_fn=list()
for i in index_list:
    i+=1
    final_fn.append(i)


finality=[]
for x in final_fn:
    y=p.index(x)
    finality.append(y)

    

axablade=list()

for i in finality:
    i=i+1
    axablade.append(i)


result=list()
for i in axablade:
    i=str(i)
    result.append(i)

for z in result:
    print(z)


# In[ ]:




