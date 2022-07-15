from linkedlist import *

class Stack:
    # Initialise an attribute that uses the LinkedList class
    def __init__(self):
        self.stack = LinkedList()
        
    def is_empty(self):
        # Returns True if the stack is empty and False otherwise
        return self.stack.is_empty()
        
    def push(self,element):
        # Add an element at the beginning of the stack.
        self.stack.insert_first(element)
        
    def pop(self):
        # Remove an element and return that removed element
        # Note: Removes the first element in the stack
        return self.stack.delete_first()
        
    def print_stack(self):
        self.stack.print_list()


def use_stack():
    s = Stack()
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