class QueueList:
    """
    A similar implementation to using a linkedlist.
    The Queue will be inefficient because inserting and deleting items from a list
    takes worst case time of O(n).
    """
    def __init__(self):
        # Initialise an empty list
        self.queue = []
        
    def is_empty(self):
        # Check if empty and return True or False
        if len(self.queue) == 0:
            return True
        else:
            return False
        
    def enqueue(self, element):
        # Add elements to the tail of the queue
        self.queue.insert(0, element)
        
    def dequeue(self):
        # Remove element from the head of the queue
        return self.queue.pop()
        
    def print_queue(self):
        print(self.queue)
        
        
def use_queue():
    q = QueueList()
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