#!/usr/bin/env python
# coding: utf-8

# In[5]:


list = ["one", 'two', 'three', 'four']
for i in range(len(list) - 1):
    print(list[i])


# In[ ]:


# i do not know why this prints these things with this replication
for i in range(len(list)):
# says that an action will be taken for every element of the list
    for j in range(i + 1):
# says that an action will be taken for every element of the range from 0 to (incl.) the index of the current element
        print(list[i])
# says that the action will be the printing of the element with the given index from the list

# maybe this is why:
# the second line adds a new layer of repeating; the whole thing says "for every number from 0 to 3,
# for every number from 0 to the current number, print the corresponding member of the list"
# but why doesnt the code come out like this:
    # one, one two, one two three, one two three four?


# In[10]:


for i in range(len(list)):
    for j in range(i + 1):
        # i = 0 -> range(1) -> j = 1
        # print list[i] for every member of the range, 1 member, for i = 0 print list[i] once
        # i = 1 -> range(2)
        print(list[i])
# i get it now!


# In[6]:


for i in range(len(list)):
    for j in range(i + 1):
        if j % 2 == 0:
            print(list[i])


# In[ ]:




