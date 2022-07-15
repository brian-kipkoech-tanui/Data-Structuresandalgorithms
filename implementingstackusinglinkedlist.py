from linkedlist import *

class Stack:
    # insert code here
    def __init__(self):
        self.stack = LinkedList()
        
    def is_empty(self):
        return self.stack.is_empty()
        
    def push(self,element):
        self.stack.insert_first(element)
        
    def pop(self):
        return self.stack.delete_first()
        
    def print_stack(self):
        self.stack.print_list()


class StackList:
    def __init__(self):
        self.stack = []
        
    def is_empty(self):
        # insert code here
        if len(self.stack) == 0:
            return True

    def push(self, element):
        # insert code here
        self.stack.append(element)
        
    def pop(self):
        # insert code here
        return self.stack.pop()
        
    def print_stack(self):
        print(self.stack)
    

def use_stack():
    s = StackList()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.print_stack()
    while not s.is_empty():
        s.pop()
    s.print_stack()
    
if __name__ == "__main__":
    use_stack()