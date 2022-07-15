linkedlist
- A linkedlist is a sequential list of nodes that hold data which point to other nodes also containing data
- The last node always has the null reference
- We always maintain a refence to the head of the linked list
- Where are linked lists used?
1) Implementation of stacks and queues
2) Mostly used as an implementation of adjacency lists for graphs.
3) Useful in creating circular lists.

Stack
(Book: Data Structures and Algorithms in Python - Michale T. GoodRich, Robert Tamassia, Michael H. GoldWasser)
- A stack is a collection of objects that are inserted and removed according to the LIFO(last-in, first-out)
- A Stack is an Abstract Data Structure(ADT) such that an instance S supports the following two methods:
1) S.push(e) - Add element e to the top of stack S
2) S.pop() - Remove and return the top element from the stack S, an error occurs if the stack is empty.

Queue:
- A Queue is a linera structure that follows a specific order in which the operations are performed.
- The order is first in first out(FIFO).
- The main difference between stacks and queues is that stacks follow LIFO while queues follow FIFO structure.
methods:
1) enqueue: To place a thing into a queue, that is adding an element to the tail of the queue.
2) dequeue: To take a thing out of a queue; thats is to remove first avalilable item from the head of a queue.