from constants import *
import pygame
import math

mode = "add"
color = RED
def setMode(m):
    global mode
    mode = m

class Button:
    def __init__(self, x, y, color, diameter=BUTTON_SIZE):
        self.x = x
        self.y = y
        self.diameter = diameter
        self.color = color

    def distToMouse(self, mouseX, mouseY):
        return math.sqrt((mouseX - self.x) ** 2 + (mouseY - self.y) ** 2)

    def onClick(self):
        pass

    def render(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.diameter/2)

class AddButton(Button):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def onClick(self):
        global color
        setMode("add")
        color = self.color

class MoveButton(Button):
    def __init__(self, x, y):
        super().__init__(x, y, GREEN)
        self.move_symbol_surface = pygame.transform.scale(pygame.image.load("move.png"), (BUTTON_SIZE-10, BUTTON_SIZE-10))

    def onClick(self):
        setMode("move")

    def render(self, surface):
        super().render(surface)
        surface.blit(self.move_symbol_surface, (self.x-self.diameter/2+5, self.y-self.diameter/2+5))

class DeleteButton(Button):
    def __init__(self, x, y):
        super().__init__(x, y, WHITE)
        self.trash_can_surface = pygame.transform.scale(pygame.image.load("assets/images/trash-can.png"), (BUTTON_SIZE - 16, BUTTON_SIZE - 16))

    def onClick(self):
        setMode("delete")

    def render(self, surface):
        super().render(surface)
        surface.blit(self.trash_can_surface, (self.x-self.diameter/2+8, self.y-self.diameter/2+8))

buttonsList = [AddButton(X_img+SIDEBAR_WIDTH/4, SIDEBAR_WIDTH/2, RED), AddButton(X_img+3*SIDEBAR_WIDTH/4, SIDEBAR_WIDTH/2, BLUE),
               MoveButton(X_img+SIDEBAR_WIDTH/4, SIDEBAR_WIDTH), DeleteButton(X_img+3*SIDEBAR_WIDTH/4, SIDEBAR_WIDTH)]

def clickButtonAction(mouseX, mouseY):
    for button in buttonsList:
        if button.distToMouse(mouseX, mouseY) <= button.diameter/2:
            button.onClick()
            return True
    return False

def render(surface):
    for button in buttonsList:
        button.render(surface)