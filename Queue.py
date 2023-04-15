#!/usr/bin/env python
# coding: utf-8

# In[172]:


class Queue():
    
    def __init__(self):
        self.elements = []
        
    def isEmpty(self):
        return self.elements == []
    
    def enqueue(self, element):
        self.elements.insert(0,element)
    
    def dequeue(self):
        return self.elements.pop()
    
    def size(self):
        return len(self.elements)
    
    def clear(self):
        return self.elements.clear()


# In[173]:


myQueue = Queue()
myQueue.clear()
myQueue.enqueue(5)  # [5]
myQueue.enqueue(4)  # [4,5]
myQueue.enqueue(1)  # [1,4,5]
myQueue.dequeue()   # [1,4]       

