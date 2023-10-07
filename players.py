import pygame.draw

import players
from constants import *
import math

playerList = []
selectedPlayer = None

class Player:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = 15
        self.border = 2

    def render(self, surface):
        pygame.draw.circle(surface, BLACK, (self.x, self.y), self.radius+self.border)
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def distToMouse(self, mouseX, mouseY):
        return math.sqrt((mouseX - self.x) ** 2 + (mouseY - self.y) ** 2)

    def setPos(self, x, y):
        self.x = x
        self.y = y

class Ball(Player):
    def __init__(self):
        super().__init__(BALL_START_COORDS[0], BALL_START_COORDS[1], BLACK)
        self.ball_surface = pygame.transform.scale(pygame.image.load("assets/images/ball.png"), (self.radius*2, self.radius*2))

    def render(self, surface):
        surface.blit(self.ball_surface, (self.x-self.radius, self.y-self.radius))


def addPlayer(player):
    playerList.append(player)

def render(surface):
    for player in playerList:
        player.render(surface)

def clickInMoveMode(mouseX, mouseY):
    global selectedPlayer
    if selectedPlayer is None:
        for player in playerList:
            if player.distToMouse(mouseX, mouseY) <= player.radius:
                selectedPlayer = player
                return
    else:
        selectedPlayer = None

def clickInDeleteMode(mouseX, mouseY):
    for player in playerList:
        if type(player) == players.Ball:
            continue
        if player.distToMouse(mouseX, mouseY) <= player.radius:
            playerList.remove(player)