#!/usr/bin/env python
# coding: utf-8

# In[27]:


# i initially made the power to which the input would raised = 16. then, i asked my dad what he thought 4^16 was.
# he said forty=seven billion. i realized i could write a log function to determine which power of 4 would actually give 4.7x10^10.
def awesomefunction(x):
    return x**17.726


# In[28]:


a = awesomefunction(4)
print(a)


# In[33]:


import math
def greatfunction(x):
    return math.log(x,4)


# In[36]:


a = greatfunction(47000000000)
print(a)


# In[44]:


# this is a functionalized version of my BMI calculator for Reverend Gwyon. I hope he starts exercising.
def bmi_calculator(weight, height, name):
    bmi = weight / (height**2)
    print("BMI:")
    print(bmi)
    if bmi > 30:
        return name + " is quite massive."
    elif bmi < 30:
        return name + " is light as a feather!"


# In[47]:


gwyon_bmi = bmi_calculator(300, 1, "Rev. Gwyon")
weight = 300
height = 1
print(gwyon_bmi)


# In[ ]:




