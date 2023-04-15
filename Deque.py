#!/usr/bin/env python
# coding: utf-8

# In[252]:


class Deque():
    
    def __init__(self):
        self.elements = []
    
    def isEmpty(self):
        return self.elements == []
    
    def addRight(self, element):
        self.elements.append(element)
    
    def addLeft(self, element):
        self.elements.insert(0,element)
    
    def removeRight(self):
        return self.elements.pop()
    
    def removeLeft(self):
        return self.elements.pop(0)
    
    def size(self):
        return len(self.elements)
    
    def clear(self):
        return self.elements.clear()


# In[253]:


myDeque = Deque()
myDeque.clear()     
myDeque.addLeft(2)   # [2]
myDeque.addRight(3)  # [2,3]
myDeque.addLeft(1)   # [1,2,3]


# In[254]:


myDeque.removeRight() # [1,2]
myDeque.removeLeft() # [2]


# In[ ]:




