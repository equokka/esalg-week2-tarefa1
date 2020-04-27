from random import choice as rchoice
from random import shuffle
from itertools import chain as flatten

from robot import Robot
from queue import Queue
from table import Table
from item import Item

class System:
  def __init__(self):
    self.queue_a = Queue()
    self.queue_b = Queue()
    self.table   = Table()
    self.robot   = Robot(self.queue_a, self.queue_b, self.table)

  def gen_queue_a(self, n):
    self.queue_a.empty()
    a = list(map(
      lambda x: Item(x),
      flatten.from_iterable([[0,1,2,3] for i in range(n)])
    ))
    shuffle(a)
    self.queue_a.receive_many(a)

  def process(self, times):
    for _ in range(times):
      self.robot.process()
