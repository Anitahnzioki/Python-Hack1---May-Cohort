class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def reverse_string(s: str) -> str:
    stack = Stack()
    for char in s:
        stack.push(char)
    reversed_str = ''
    while not stack.is_empty():
        reversed_str += stack.pop()
    return reversed_str


class QueueWithStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int):
        self.stack1.append(x)

    def dequeue(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise IndexError("dequeue from empty queue")
        return self.stack2.pop()


class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def find_max(self) -> int:
        if not self.head:
            raise ValueError("LinkedList is empty")
        max_value = self.head.value
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value

readme/Steps explanations

Original file line number	Diff line number	Diff line change
@@ -0,0 +1,17 @@
Task 1: Reverse a String Using a Stack
Explanation;
Stack Class: Implements a basic stack with methods to push items, pop items, and check if the stack is empty.
reverse_string Function:Initializes a stack.Pushes each character of the input string onto the stack.Pops each character from the stack to build the reversed string.
The stack follows Last In, First Out (LIFO) order, so when characters are popped from the stack, they come out in reverse order of their input.
Task 2: Implement a Queue Using Two Stacks
Explanation;
QueueWithStacks Class:Uses two stacks (stack1 and stack2) to simulate queue operations.
enqueue Method: Adds an element to stack1.
dequeue Method:If stack2 is empty, moves all elements from stack1 to stack2 (reversing their order).Pops and returns the top element from stack2. If both stacks are empty, raises an exception.
This method allows the queue to maintain FIFO order by reversing the order of elements between the two stacks.
Task 3. Find the Maximum Element in a List Using a Linked List
Explanation
Node Class: Represents a node in the linked list with a value and a pointer to the next node.
LinkedList Class:
append Method: Adds a new node to the end of the list.
find_max Method:Traverses the linked list from the head to find and return the maximum value.
