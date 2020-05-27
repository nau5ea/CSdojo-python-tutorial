#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = 3
b = 2
while b <= 5:
    a += b
    b *= 2
print(a)


# In[2]:


amazinglist = [2, 4, 6, 8, 10, 11, 13, 15, 17]


# In[5]:


for c in amazinglist:
    if c % 2 == 0:
        c += amazinglist[5]
print(amazinglist)


# In[22]:


awesome_list = [-3, -3, -3, 4, -3, -3, 1]


# In[15]:


print(awesome_list[0])


# In[16]:


# trying to sum every other element of awesome_list; result should be -9
total = 0
a = 0
while awesome_list[a] < 0:
    total += awesome_list[a]
    a += 2
print(total)


# In[ ]:


# it did not work


# In[19]:


total = 0
a = 0
while a < len(awesome_list) and awesome_list[a] < 0:
    total += awesome_list[a]
    a += 2
print(total)


# In[18]:


# sweet!! finally a success. i was working on while loops all day without satisfaction


# In[25]:


total1 = 0
for i in awesome_list:
    if i < 0:
        break
    total1 += i
print(total1)


# In[38]:


# YK's challenge: find the sum of the negative elements of this list:
greatlist = [7, 5, 5, 4, 3, 2, 1, 0, -1, -2, -3, -5, -5, -5, -7]
total = 0
index = len(greatlist)
while greatlist[index] < 0:
    total += greatlist[index]
    index -= 1
print(total)


# In[39]:


# above didn't work due to index out of range error
print(greatlist[index])
# apparently, the called index cannot be defined as len(the list)


# In[41]:


greatlist = [7, 5, 5, 4, 3, 2, 1, 0, -1, -2, -3, -5, -5, -5, -7]
total = 0
index = len(greatlist) - 1
while greatlist[index] < 0:
    total += greatlist[index]
    index -= 1
print(total)
# desired result achieved by defining index var as 1 less than len(the list)


# In[46]:


# greatlist = [7, 5, 5, 4, 3, 2, 1, 0, -1, -2, -3, -5, -5, -5, -7]
total = 0
for element in greatlist:
    if element <= 0:
        total += element
print(total)
# u can do it with a for loop too!


# In[ ]:




