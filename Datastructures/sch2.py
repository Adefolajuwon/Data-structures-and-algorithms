class Queue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def enqueue(self, value):
        self.elements.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.elements.pop(0)

    def front(self):
        if self.is_empty():
            return None
        return self.elements[0]

    def show(self):
        print("Current Queue:", self.elements)

# Example usage
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("Queue at start:")
q.show()

removed_item = q.dequeue()
print(f"Item removed: {removed_item}")
print("Queue after removing an item:")
q.show()
