from collections import deque

import pygame

import screen

class App(screen.RootScreen):
  APP_EVENT = pygame.locals.USEREVENT + 1
  def __init__(self, window_size):
    pygame.init()
    self.disp = pygame.display.set_mode(window_size)
    self.clock = pygame.time.Clock()
    self.FPS = 60
    self.event = None
    super().__init__(self)

  def draw(self):
    self.disp.fill((255, 255, 255))
    super().draw()
    pygame.display.flip()

  def loop(self):
    while True:
      draw = False
      for self.event in pygame.event.get():
        draw = True
        self.proc()
      if draw or self.state.get("NEED_REDRAW", False):
        self.draw()
      self.clock.tick(self.FPS)
  
  def 

