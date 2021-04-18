from collections import deque

import pygame

import screen

class App(screen.RootScreen):
  def __init__(self, window_size):
    pygame.init()
    self.disp = pygame.display.set_mode(window_size)
    self.clock = pygame.time.Clock()
    self.FPS = 60
    self.event = deque()
    super().__init__(self)

  def proc(self):
    if self.event or self.state["NEED_REDRAW"]:
      self.draw()

  def draw(self):
    self.disp.fill((255, 255, 255))
    super().draw()
    pygame.display.flip()

  def loop(self):
    while True:
      for event in pygame.event.get():
        self.event.append(event)
      self.proc()
      self.clock.tick(self.FPS)