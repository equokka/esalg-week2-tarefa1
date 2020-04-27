class Stack:
  def __init__(self):
    self.stack = []

  def __str__(self):
    return str(self.stack)

  def receive(self, item):
    return self.stack.append(item)

  def receive_many(self, items):
    for i in items:
      self.receive(i)

  def give(self, item):
    return self.stack.pop(item)

  def peek(self):
    return self.stack[0]

  def size(self):
    return len(self.stack)

  def empty(self):
    self.stack = []

# a = Queue()
# a.receive_many([2,2,34,4])
# print(a)
