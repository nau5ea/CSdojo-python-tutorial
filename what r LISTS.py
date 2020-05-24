#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = ["skip a few", 100, 99]


# In[2]:


b = a[1]


# In[3]:


a[1] = a[2]


# In[4]:


a[2] = b


# In[5]:


print(a)


# In[14]:


# here i used simple temp-variable switching to count to 100.
c = [100, 2, 99, 1, 'skip a few']


# In[15]:


d = c[0]
e = c[3]


# In[16]:


c[0] = e
f = c[4]
g = c[2]


# In[17]:


print(c)


# In[18]:


c[2] = f
c[3] = g
c[4] = d


# In[19]:


print(c)

