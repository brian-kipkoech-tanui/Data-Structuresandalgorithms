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
a) S.push(e) - Add element e to the top of stack S
b) S.pop() - Remove and return the top element from the stack S, an error occurs if the stack is empty.