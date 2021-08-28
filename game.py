import pygame
import sys

from menu import Menu


WIDTH = 960
HEIGHT = 540


def button_one_clicked():
    print("BUTTON CLICKED")


class Game:
    def __init__(self):
        self.running = True

        pygame.init()
        pygame.display.set_caption("Menu Tutorial")
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))

        self.menu = Menu(100, 100)
        self.menu.add_button("A Button", button_one_clicked)
        self.menu.add_button("Quit", self.quit)

    def run(self):
        while self.running:
            self.surface.fill((255, 255, 255))

            events = pygame.event.get()
            self.handle_events(events)
            self.menu.on_render(self.surface)

            pygame.display.flip()

        pygame.quit()
        sys.exit()

    def handle_events(self, events):
        pos = pygame.mouse.get_pos()

        for e in events:
            if e.type == pygame.QUIT:
                self.quit()
            elif e.type == pygame.MOUSEMOTION:
                self.menu.on_mouse_move(pos)
            elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                self.menu.on_mouse_press(pos)
            elif e.type == pygame.MOUSEBUTTONUP and e.button == 1:
                self.menu.on_mouse_release(pos)

    def quit(self):
        self.running = False
