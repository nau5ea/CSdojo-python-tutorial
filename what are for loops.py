#!/usr/bin/env python
# coding: utf-8

# In[27]:


awesomelist = ["swag", "1", "2" , "3"]
# i tried to add 2 to each element of the list


# In[28]:


# here is the original
for element in awesomelist:
    element + "2" # this of course will not add 2 to the elements as numbers, but will concatenate them as strings?
    print(element)


# In[29]:


# didnt work, let's try naming them differently


# In[30]:


for a in awesomelist:
    a + "2"
    print(element)
# the mistake here is not changing the printed variable from "element" after i switched the variable used in the for-part.
# for some reason it made them all 3!


# In[39]:


for a in awesomelist:
    a + "2"
    print(a)
# back to normal


# In[36]:


b = "2"
for a in awesomelist:
    print(a + b)
# eureka


# In[41]:


# same result, different method:
for a in awesomelist:
    a += "2"
    print(a)


# In[47]:


# a modulo-operator for-loop which prints multiples of 3 from 1 to 99, and prints odd numbers greater than 2.
for x in range(1, 100):
    if x % 3 == 0:
        print(x)
    elif x % 2 == 0:
        x += 1
        print(x)


# In[53]:


# YK's challenge problem: compute the sum of multiples of 3 and 5 less than 100
    # i wonder if i could find the greatest such sum which itself in less than 100
sum1 = 0
a = list(range(1, 100))
for n in a:
    if n % 3 == 0:
        sum1 += n
    elif n % 5 == 0:
        sum1 += n
print(sum1)


# In[54]:


# someone in comments used "or" to solve the same problem, like so:
sum1 = 0
a = list(range(1, 100))
for n in a:
    if n % 3 == 0 or n % 5 == 0:
        sum1 += n
print(sum1)


# In[ ]:




