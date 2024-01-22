class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):  # Adds an element to the top of the stack.
        self.items.append(item)

    def pop(self):  # Removes the element from the top of the stack.
        if not self.is_empty():
            return self.items.pop()

    def peek(self):  # Returns the element at the top of the stack without removing it.
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):  # Checks if the stack is empty.
        return len(self.items) == 0


# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Top of the stack:", stack.peek())    # Output: 3
print("Popped element:", stack.pop())       # Output: 3
print("Stack after popping:", stack.items)  # Output: [1, 2]

# A stack is a Last In, First Out (LIFO) data structure where the last element added is the first one to be removed.
