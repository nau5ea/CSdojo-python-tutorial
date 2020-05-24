#!/usr/bin/env python
# coding: utf-8

# In[10]:


# a comparator for two people's heights
gwyon = 5
olson = 4
if olson < gwyon:
    print("Olson is shorter than Gwyon.")
else:
    if olson == gwyon:
        print("Olson and Gwyon are the same height.")
    else:
        print("Gwyon is shorter than Olson.")


# In[13]:


gwyon = 5
olson = 4
if olson < gwyon:
    print("Olson is shorter than Gwyon.")
elif olson == gwyon:
        print("Olson and Gwyon are the same height.")
else:
    print("Gwyon is shorter than Olson.")


# In[8]:


# a body mass index calculator used by the Reverend Gwyon.
name = "Rev. Gwyon"
weight = 300
height = 1

bmi = weight / (height**2)
print("BMI:")
print(bmi)
print(name)
if bmi > 30:
    print("is quite massive.")
elif bmi < 30:
    print("is light as a feather!")


# In[ ]:




