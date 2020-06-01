#!/usr/bin/env python
# coding: utf-8

# In[ ]:


webster = {}


# In[ ]:


webster["Rhododendron"] = 2


# In[ ]:


webster["Azalea"] = 12


# In[ ]:


# this was not cool tbh


# In[ ]:


# here i try to create a Ghost class whose objects will repeat boo according to their scariness value


# In[1]:


class Ghost:
    scarylist = list(range[scariness])
    def scare_human(self):
        for i in scarylist:
            print('BOO!')


# In[2]:


steve = Ghost()
steve.name = "Steve"
steve.scariness = 1000
steve.hungriness = 10


# In[3]:


steve.scare_human()


# In[4]:


# here i try to fix it:
class Ghost:
    def __init__(self, name, scariness, scarylist):
        self.name = name
        self.scariness = scariness
        self.scarylist = list(range[scariness])
    def scare_human(self):
        for i in scarylist:
            print('BOO!')


# In[5]:


scarylist = list[range(1000)]
steve = Ghost("Steve", 1000, scarylist)


# In[27]:


# I posted this problem on stackoverflow; moving onto a new idea
class Frog:
    def __init__(self, name):
        self.name = name
    def jump(self):
        print(self.name + "... has jumped...")


# In[28]:


skippy = Frog("skippy")


# In[29]:


skippy.jump()


# In[ ]:




