from stack import Stack

class Table:
  def __init__(self):
    self.stacks = {
      "tea": {
        "cup": Stack(),
        "plate": Stack()
      },
      "coffee": {
        "cup": Stack(),
        "plate": Stack()
      }
    }

  def check_compatible(self, item):
    wear = None
    if item.wear == "cup": wear = "plate"
    else:                  wear = "cup"
    return self.stacks[item.variant][wear].size() > 0

  def get_compatible(self, item):
    wear = None
    if item.wear == "cup": wear = "plate"
    else:                  wear = "cup"
    print("Peça %s retirada da pilha %s/%s" % (item, item.variant, wear))
    return self.stacks[item.variant][wear].give()

  def peek_compatible(self, item):
    wear = None
    if item.wear == "cup": wear = "plate"
    else:                  wear = "cup"
    return self.stacks[item.variant][wear].peek()

  def receive(self, item):
    self.stacks[item.variant][item.wear].receive(item)
    print("Peça %s colocada na pilha %s/%s" % (item, item.variant, item.wear))

