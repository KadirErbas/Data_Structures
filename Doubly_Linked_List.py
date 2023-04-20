#!/usr/bin/env python
# coding: utf-8

# In[180]:


class DoublyNode():
    
    def __init__(self, value):
        self.value = value
        self.nextNode = None
        self.prevNode= None
        


# In[181]:


node1 = DoublyNode(10)
node2 = DoublyNode(20)
node3 = DoublyNode(30)


# In[182]:


node1.nextNode = node2
node2.prevNode = node1
node2.nextNode = node3
node3.prevNode = node2


# In[183]:


node1.nextNode.value            # 20
node2.prevNode.value            # 10
node2.nextNode.value            # 30
node3.prevNode.value            # 20
node1.nextNode.nextNode.value   # 30

