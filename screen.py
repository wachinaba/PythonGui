import pygame as pg

import container

class Screen(container.Container):
  def __init__(self, rect, app):
    super().__init__()
    self.rect = rect
    self.surface = pg.Surface((rect.width, rect.height), pg.locals.SRCALPHA or pg.locals.HWSURFACE)
    self.app = app
    self.state = dict()
    self.state["NEED_REDRAW"] = False

  def draw_callback(self):
    self.parent.surface.blit(self.surface, self.rect)

  def proc_callback(self):
    pass

  def send_redraw(self):
    self.state["NEED_REDRAW"] = True
    if self.parent.state.get("NEED_REDRAW", True):
      return
    self.parent.send_redraw()

  def proc(self):
    self.proc_callback()
    for c in self:
      c.proc_callback()

  def draw(self):
    for c in reversed(self):
      if c.state.get("NEED_REDRAW", False):
        c.draw_callback()
        c.state["NEED_REDRAW"] = False
    self.draw_callback()

class RootScreen(Screen):
  def __init__(self, app):
    super().__init__(pg.display.get_surface(), app)

  def send_redraw(self):
    self.state["NEED_REDRAW"] = True
