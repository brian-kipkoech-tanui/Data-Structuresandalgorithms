from linkedlist import *

class Queue:
    def __init__(self):
        # Initialize the LinkedList() class
        self.queue = LinkedList()
        
    def is_empty(self):
        return self.queue.is_empty()
        
    def enqueue(self, element):
        # Add an element to the tail of the queue
        self.queue.insert_last(element)
        
    def dequeue(self):
        # Remove the first element from the head of the queue
        return self.queue.delete_first()
        
    def print_queue(self):
        self.queue.print_list()
        
        
        
def use_queue():
    q = Queue()
    q.enqueue('Brian')
    q.enqueue('Benard')
    q.enqueue('Mercy')
    q.enqueue('Tanui')
    q.enqueue('Mark')
    q.print_queue()
    q.dequeue()
    q.print_queue()
    
    
if __name__ == "__main__":
    use_queue()