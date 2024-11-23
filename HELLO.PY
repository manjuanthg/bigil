class Queue:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = 0

    def enqueue(self, item):
        "add an item to the rear of the queue"
        self.queue.append(item)
        self.rear += 1

    def dequeue(self):
        "remove and return the front item from the queue"
        if self.is_empty():
            raise IndexError("queue is empty")
        else:
            front_item = self.queue[self.front]
            self.front += 1
            return front_item

    def peek(self):
        "return the front item from the queue without removing it"
        if self.is_empty():
            raise IndexError("queue is empty")
        else:
            return self.queue[self.front]

    def is_empty(self):
        "check if the queue is empty"
        return self.front >= self.rear

    def size(self):
        "return the number of items in the queue"
        return self.rear - self.front

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("queue:", q.queue)

front_item = q.dequeue()
print("dequeue item:", front_item)
print("queue after dequeue:", q.queue)

print("front item:", q.peek())
print("queue size:", q.size())
