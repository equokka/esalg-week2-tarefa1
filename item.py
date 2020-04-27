class Item:
  def __init__(self, kind):
    self.kind = kind
    if self.kind == 0:
      self.variant = "tea"
      self.wear = "plate"
      self.bark = "Prato de Chá"
    elif self.kind == 1:
      self.variant = "coffee"
      self.wear = "plate"
      self.bark = "Prato de Café"
    elif self.kind == 2:
      self.variant = "tea"
      self.wear = "cup"
      self.bark = "Chávena de Chá"
    elif self.kind == 3:
      self.variant = "coffee"
      self.wear = "cup"
      self.bark = "Chávena de Café"
    elif self.kind == 4:
      self.variant = "tea"
      self.wear = "package"
      self.bark = "Prato e chávena de Chá (Embalado)"
    elif self.kind == 5:
      self.variant = "coffee"
      self.wear = "package"
      self.bark = "Prato e chávena de Café (Embalado)"

  def __repr__(self):
    return "<%s>" % self.bark

  def __str__(self):
    return self.bark
