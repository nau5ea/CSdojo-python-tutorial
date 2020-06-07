#!/usr/bin/env python
# coding: utf-8

# In[1]:


f = [2, 4, 6, 8, 10, 12]


# In[2]:


g = [e + 1 for e in f]


# In[3]:


print(g)


# In[4]:


j = range(100)


# In[5]:


g = [e * 2 + 1 for e in j]


# In[6]:


print(g)


# In[21]:


# built a working class which tells whether it is a sunna to eat dates in odd numbers.
class Prophet:
    def __init__(self, eating, food, numberfood):
        self.eating = eating
        self.food = food
        self.numberfood = numberfood
    def is_it_a_sunna(self):
        if self.food == "date" and self.numberfood % 2 > 0:
            print("It is said that it is a sunna to eat dates in odd numbers.")


# In[18]:


Mohamet = Prophet(True, "date", 3)
Mohamet.is_it_a_sunna()


# In[21]:


# now i want to incorporate the new list-comprehensive syntax into this class somehow.
class Prophet:
    def __init__(self, eating, food, numberfood):
        self.eating = eating
        self.food = food
        self.numberfood = numberfood
    def is_it_a_sunna(self):
        if self.food == "date" and self.numberfood % 2 > 0:
            print("It is said that it is a sunna to eat dates in odd numbers.")
    def mathematize(self):
        c = [x * 2 for x in range(self.numberfood)]        
        print(c)


# In[22]:


Mohamet = Prophet(True, "date", 3)
Mohamet.mathematize()


# In[28]:


# problem presented at the end of vido #12:
# create the list [36, 25, 16, 9, 4, 1] by append function and list comprehension
# with append:
c = []
for x in range(6, 0, -1):
    c.append(x ** 2)
print(c)


# In[31]:


# with list comp
c = [x ** 2 for x in range(6, 0, -1)]
print(c)


# In[ ]:




