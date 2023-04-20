#!/usr/bin/env python
# coding: utf-8

# In[169]:


class Node():
    
    def __init__(self, value):
        self.value = value
        self.nextNode = None
        


# In[170]:


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)


# In[171]:


node1.nextNode = node2
node2.nextNode = node3


# In[172]:


node1.nextNode.value            # 20
node2.nextNode.value            # 30
node1.nextNode.nextNode.value   # 30

