import pygame as pg

import container

class Screen(container.Container):
  def __init__(self, rect):
    super().__init__()
    self.rect = rect
    self.surface = pg.Surface((rect.width, rect.height), pg.locals.SRCALPHA or pg.locals.HWSURFACE)
    self.state["NEED_REDRAW"] = False

  def draw_callback(self):
    self.parent.surface.blit(self.surface, self.rect)

  def send_redraw(self):
    self.state["NEED_REDRAW"] = True
    if self.parent.state.get("NEED_REDRAW", True):
      return
    self.parent.send_redraw()

  def proc(self):
    if self.state.get()


class RootScreen(Screen):
  def __init__(self):
    super().__init__(pg.display.get_surface())
