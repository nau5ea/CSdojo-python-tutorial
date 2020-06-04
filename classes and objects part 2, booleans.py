#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Person:
    def __init__(self, swag, name, falling):
        self.name = name
        self.swag = swag
        self.falling = falling
    def Fall(self):
        self.falling = True
    def Land(self):
        self.falling = False
    def IdentityCrisis(self):
        self.name = "n/a"
    def Selfdisclosure(self):
        print(self.swag, self.name, self.falling)


# In[ ]:


alice = Person("swaggy", "Engels", True)
alice.Selfdisclosure()


# In[ ]:


robot = Person("metal", "REH43", False)


# In[ ]:


robot.creator = alice


# In[ ]:


robot.creator.Selfdisclosure()


# In[17]:


def c_greater_than_d_plus_e(c, d, e):
    return c > d + e


# In[18]:


c_greater_than_d_plus_e(2, 2, 2)


# In[19]:


c_greater_than_d_plus_e(2, 2, 2)


# In[ ]:




