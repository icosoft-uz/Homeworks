from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):  # Adds an element to the rear (end) of the queue.
        self.items.append(item)

    def dequeue(self):  # Removes the element from the front of the queue.
        if not self.is_empty():
            return self.items.popleft()

    def front(self):  # Returns the element at the front of the queue without removing it.
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):  # Checks if the stack is empty.
        return len(self.items) == 0


# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Front of the queue:", queue.front())  # Output: 1
print("Dequeued element:", queue.dequeue())  # Output: 1
print("Queue after dequeue:", queue.items)  # Output: deque([2, 3])

# A queue is a First In, First Out (FIFO) data structure where the first element added is the first one to be removed.
