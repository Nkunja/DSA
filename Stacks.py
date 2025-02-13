"""
A Stack is a data structure that follows the Last In First Out (LIFO) principle. 
A stack is a Data Structure that can hold many elements

Basic Operations are:
    push(element): Add an element to the top of the stack
    pop(): Remove and return the top element from the stack
    peek(): Return the top element of the stack without removing it
    is_empty(): Check if the stack is empty
    size(): Return the number of elements in the stack
    display(): Print all the elements in the stack from top to bottom
    reverse(): Reverse the order of elements in the stack without using any additional data structures
    
    
Stacks can be used to implement undo mechanisms, to revert to previous states, to create algorithms for depth-first search in graphs, or for backtracking.

Reasons to implement stacks using arrays:
    Memory Efficient: Array elements do not hold the next elements address like linked list nodes do.
    Easier to implement and understand: Using arrays to implement stacks require less code than using linked lists, and for this reason it is typically easier to understand as well.
    
A reason for using linked lists to implement stacks:

    Dynamic size: The stack can grow and shrink dynamically, unlike with arrays.
Reasons for not using linked lists to implement stacks:

    Extra memory: Each stack element must contain the address to the next element (the next linked list node).
    Readability: The code might be harder to read and write for some because it is longer and more complex.

"""

#One

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)

# Create a stack
myStack = Stack()

myStack.push('A')
myStack.push('B')
myStack.push('C')
print("Stack: ", myStack.stack)

print("Pop: ", myStack.pop())

print("Peek: ", myStack.peek())

print("isEmpty: ", myStack.isEmpty())

print("Size: ", myStack.size())


# Two - linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value
    
    def isEmpty(self):
        return self.size == 0
    
    def stackSize(self):
        return self.size

myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')

print("Pop: ", myStack.pop())
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.stackSize())