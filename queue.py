from collections import deque
# https://docs.python.org/3/library/collections.html#collections.deque

class Queue:
  def __init__(self):
    self.queue = deque([])

  def __str__(self):
    return str(list(self.queue))

  def receive(self, item):
    return self.queue.appendleft(item)

  def receive_many(self, items):
    for i in items:
      self.receive(i)

  def give(self, item):
    return self.queue.pop(item)

  def peek(self):
    return self.queue[-1]

  def size(self):
    return len(self.queue)

  def empty(self):
    self.queue = deque([])

# a = Queue()
# a.receive_many([2,2,34,4])
# print(a)
