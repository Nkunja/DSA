"""
Description: This file contains the implementation of the Queue data structure.

A Queue is a data structure that follows the First In First Out (FIFO) principle. 
It can hold many elements

Basic Operations on Queues are:
    \n1. enqueue(element): Add an element to the rear of the queue
    \n2. dequeue(): Remove and return the element from the front of the queue
    \n3. is_empty(): Check if the queue is empty
    \n4. size(): Return the number of elements in the queue
    \n5. peek(): Return the element at the front of the queue without removing it
    \n6. display(): Print all elements in the queue from front to rear
    \n7. reverse(): Reverse the order of elements in the queue
    \n8. sort(): Sort the elements in the queue in ascending order
    
Queues can be implemented by using arrays or linked lists.

Queues can be used to implement job scheduling for an office printer, order processing for e-tickets, or to create algorithms for breadth-first search in graphs.

Reasons to implement queues using arrays:
    Memory Efficient: Array elements do not hold the next elements address like linked list nodes do.
    Easier to implement and understand: Using arrays to implement queues require less code than using linked lists, and for this reason it is typically easier to understand as well.
    
Reasons for not using arrays to implement queues:
    Fixed size: An array occupies a fixed part of the memory. This means that it could take up more memory than needed, or if the array fills up, it cannot hold more elements. And resizing an array can be costly.
    Shifting cost: Dequeue causes the first element in a queue to be removed, and the other elements must be shifted to take the removed elements' place. This is inefficient and can cause problems, especially if the queue is long.
    Limited functionality: Some queue operations, such as reversing or sorting, are not possible with arrays.
Alternatives: Some programming languages have built-in data structures optimized for queue operations that are better than using arrays

Reasons for using linked lists to implement queues:
    Dynamic size: The queue can grow and shrink dynamically, unlike with arrays.
    No shifting: The front element of the queue can be removed (enqueue) without having to shift other elements in the memory.
    
Reasons for not using linked lists to implement queues:
    Extra memory: Each queue element must contain the address to the next element (the next linked list node).
    Readability: The code might be harder to read and write for some because it is longer and more complex.

"""

# Queue using Arrays Implementation

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        self.queue.append(element)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

# Create a queue
myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
print("Queue: ", myQueue.queue)

print("Dequeue: ", myQueue.dequeue())

print("Peek: ", myQueue.peek())

print("isEmpty: ", myQueue.isEmpty())

print("Size: ", myQueue.size())


# Queue using Linked List Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    
    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
            self.length += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return temp.data
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.data
    
    def isEmpty(self):
        return self.length == 0
    
    def size(self):
        return self.length

    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Create a queue
myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
print("Queue: ", end="")
myQueue.printQueue()

print("Dequeue: ", myQueue.dequeue())

print("Peek: ", myQueue.peek())

print("isEmpty: ", myQueue.isEmpty())

print("Size: ", myQueue.size())