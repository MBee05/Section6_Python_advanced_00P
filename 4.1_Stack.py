# # List
# l=[1,2]
# print(l)        #[1, 2]

# print(l.append(3))
# print(l)        #[1, 2, 3]

# print(l.pop())  #3
# print(l)        #[1, 2]

# print(l.insert(0,4))  #3
# print(l)              #[4, 1, 2]



"""whatever goes last comes out first"""

class Stack(object):
    def __init__(self):
        self.item=[]
        
    def push(self,item=''):
        """ param item: accepts as paramater
        Push the elements at the last index
        return: none"""
        
        self.item.append(item)
        
        
    def pop(self):
        """ this will remove last item
        return: none"""
        
        self.item.pop()
        pass
    
    def peek(self):
        """Allows us to see the last elements 
        return: last item"""
        if self.item:
            return self.item[-1]
        else:
            return None
         
   
    def size(self):
        """Allows us to see the last elements 
        return: last item"""
        if self.item:
            return len(self.item)
        else:
            return None
        
    def isempty(self):
        """tells whether the stack is empty or not 
        return Bool Value"""
        if self.item == []:
            return True
        else:
            return False
        
if __name__== "__main__":
    stack=Stack()
    stack.push("1")
    stack.push('2')
    print(stack.size())     #2
    print(stack.peek())     #2
    
    
    stack.pop()
    print(stack.size())     #1
    print(stack.peek())     #1
    
    print(stack.isempty())  #False
    stack.pop()
    print(stack.isempty())  #True

        
    
    
    
    
            