from button import Button


class Menu:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.button_width = 200
        self.button_height = 40
        self.buttons = []

    def add_button(self, text, callback):
        self.buttons.append(Button(text, callback, self.x, self.y, self.button_width, self.button_height))
        self.y += self.button_height + 8

    def get_button_at(self, pos):
        for i in range(len(self.buttons)):
            button = self.buttons[i]
            if button.collidepoint(pos):
                return i

    def on_mouse_move(self, pos):
        for button in self.buttons:
            if button.collidepoint(pos):
                button.on_mouse_over()
            else:
                button.on_mouse_off()

    def on_mouse_press(self, pos):
        for button in self.buttons:
            if button.collidepoint(pos):
                button.on_mouse_press()
                return

    def on_mouse_release(self, pos):
        for button in self.buttons:
            if button.collidepoint(pos):
                button.on_mouse_release()
                return

    def on_render(self, surface):
        for button in self.buttons:
            button.on_render(surface)

