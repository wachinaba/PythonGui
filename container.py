class Container():
  def __init__(self):
    self._next = None
    self._prev = None

    self.childs = None
    self._childs_len = 0

  def __len__(self):
    return self._childs_len

  def append(self, container):
    container._next = self.childs
    
    


  
