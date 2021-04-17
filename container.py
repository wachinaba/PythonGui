class Node():
  def __init__(self):
    self.prev = None
    self.next = None

class Container(Node):
  class AttachError(Exception):
    pass
  class DetachError(Exception):
    pass

  def __init__(self):
    super().__init__()

    self.parent = None
    self.childs_head = Node()
    self.childs_len = 0

  def __len__(self):
    return self.childs_len

  def attach(self, parent):
    if self.parent:
      raise Container.AttachError("The container already has been in another deque")

    self.parent = parent
    self.prev, self.next = parent.childs_head, parent.childs_head.next
    parent.childs_head.next.prev = parent.childs_head.next = self
    parent.childs_len += 1

  def detach(self):
    if not self.parent:
      raise Container.DetachError("The container doesn't have a parent")
    self.prev.next = self.next
    self.next.prev = self.prev
    self.parent.childs_len -= 1
    self.prev = self.next = self.parent = None
  
  def move_top(self):
    self.prev.next = self.next
    self.next.prev = self.prev
    self.prev, self.next = self.parent.childs_head, self.parent.childs_head.next
    self.parent.childs_head.next.prev = self.parent.childs_head.next = self

  def __iter__(self):
    return Container.Iterator(self)

  def __reversed__(self):
    return Container.ReversedIterator

  class Iterator():
    def __init__(self, container):
      self.container = container
      self.next = container.childs_head

    def __iter__(self):
      return self

    def __next__(self):
      self.next = self.next.next
      if not self.next == self.container.childs_head:
        return self.next
      else:
        raise StopIteration

  class ReversedIterator(Iterator):
    def __init__(self, container):
      super().__init__(container)

    def __next__(self):
      self.next = self.next.prev
      if not self.next == self.container.childs_head:
        return self.next
      else:
        raise StopIteration
    