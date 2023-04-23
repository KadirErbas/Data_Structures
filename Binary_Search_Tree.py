#!/usr/bin/env python
# coding: utf-8

# In[17]:


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        


# In[102]:


class BinarySearchTree():
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        
        newNode = Node(value)
        
        if self.root == None:
            self.root = newNode
            return True
        
        tempNode = self.root
        
        while True:
            if newNode.value == tempNode.value:
                return False
            
            elif newNode.value < tempNode.value:
                if tempNode.left is None:
                    tempNode.left = newNode
                    return True
                else:
                    tempNode = tempNode.left
            
            elif newNode.value > tempNode.value:
                if tempNode.right == None:
                    tempNode.right = newNode
                    return True
                else:
                    tempNode = tempNode.right
    
   
    def contains(self,value):
        tempNode = self.root
        
        while tempNode:
            if value == tempNode.value:
                return True
            elif value < tempNode.value:
                tempNode = tempNode.left
            else:
                tempNode = tempNode.right
        return False
    
    
    def minOfNode(self):
        tempNode = self.root
        
        while tempNode.left:
            tempNode = tempNode.left        
        return tempNode.value
    
    
    def maxOfNode(self):
        tempNode = self.root
        
        while tempNode.right:
            tempNode = tempNode.right       
        return tempNode.value


# In[103]:


myTree = BinarySearchTree()


# In[104]:


myTree.insert(3)
myTree.insert(2)
myTree.insert(1)
myTree.insert(5)
myTree.insert(4)


# In[105]:


myTree.minOfNode()


# In[106]:


myTree.maxOfNode()

