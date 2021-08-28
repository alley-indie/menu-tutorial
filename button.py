import pygame

from image import slice_and_assemble


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (155, 155, 155)
DARK_GRAY = (55, 55, 55)


class Button:
    def __init__(self, text, callback, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.callback = callback

        font = pygame.font.Font("AtariClassicChunky-PxXP.ttf", 20)
        self.text = font.render(text, True, WHITE)

        self.backgrounds = slice_and_assemble("button.png", (24, 24), (8, 8), (width, height))
        self.current_bg = 0

    def collidepoint(self, pos):
        return self.rect.collidepoint(pos)

    def on_mouse_over(self):
        self.current_bg = 1

    def on_mouse_off(self):
        self.current_bg = 0

    def on_mouse_press(self):
        self.current_bg = 2

    def on_mouse_release(self):
        self.current_bg = 0
        if self.callback is not None:
            self.callback()

    def on_render(self, surface):
        surface.blit(self.backgrounds[self.current_bg], self.rect)

        pos = (
            self.rect.x + (self.rect.width - self.text.get_width()) // 2,
            self.rect.y + (self.rect.height - self.text.get_height()) // 2
        )
        surface.blit(self.text, pos)
