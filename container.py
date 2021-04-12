class Node():
  def __init__(self):
    self.prev = None
    self.next = None

class Container(Node):
  class AppendError(Exception):
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
      raise Container.AppendError("The container already has been in another deque")

    self.parent = parent
    self.prev, self.next = parent.childs_head, parent.childs_head.next
    parent.childs_head.next.prev = parent.childs_head.next = self
    parent.childs_len += 1

  def detach(self):
    self.prev.next = self.next
    self.next.prev = self.prev
    self.parent.childs_len -= 1
    self.prev = self.next = self.parent = None
  
  def move_top(self):
    self.prev.next = self.next
    self.next.prev = self.prev
    self.prev, self.next = self.parent.childs_head, self.parent.childs_head.next
    self.parent.childs_head.next.prev = self.parent.childs_head.next = self
