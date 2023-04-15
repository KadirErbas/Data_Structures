#!/usr/bin/env python
# coding: utf-8

# In[75]:


class Stack():
    
    def __init__(self):
        self.elements = []
            
    def isEmpty(self):
        return self.elements == []
    
    def push(self, element):
        self.elements.append(element)
    
    def pop(self):
        return self.elements.pop()
    
    def showLast(self):
         return self.elements[-1]
    
    def size(self):
        return len(self.elements)


# In[85]:


myStack = Stack()
myStack.push(9)
myStack.pop()


# In[ ]:




