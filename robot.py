class Robot:
  # left and right are Queues
  # pile is a Stack
  def __init__(self, right, left, table):
    self.right = right
    self.left = left
    self.table = table
    self.touched_count = 0
    self.package_count = 0

  def process(self):

    if self.table.check_compatible(self.right.peek()):

      v = None
      if self.right.variant == "tea": v = 4
      else:                           v = 5

      i = Item(self, v)

      print("Peças %s e %s juntas em %s, colocado no tapete B" % (self.right.peek(), self.table.peek_compatible(), i))

      self.table.get_compatible(self.right.peek())
      self.right.peek.give()

      self.left.receive(i)
      self.package_count += 1

    else:
      self.table.receive(self.right.give())

    self.touched_count += 1
