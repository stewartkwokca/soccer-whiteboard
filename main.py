# Field: https://pixabay.com/vectors/soccer-field-diagram-green-307046/
# Arrows: <a href="https://www.flaticon.com/free-icons/move-selection" title="move selection icons">Move selection icons created by Design Circle - Flaticon</a>
# Trash Can: <a href="https://www.flaticon.com/free-icons/trash" title="trash icons">Trash icons created by Freepik - Flaticon</a>

import pygame
import players
from constants import *

pygame.init()
screen = pygame.display.set_mode((X_img + SIDEBAR_WIDTH, Y_img))
pygame.display.set_caption("Soccer Whiteboard")

import buttons

players.addPlayer(players.Ball())

field_surface = pygame.image.load("assets/images/field.png")

running = True

while running:
    screen.fill(BLACK)
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if buttons.clickButtonAction(mouse[0], mouse[1]):
                pass
            elif buttons.mode == "add" and mouse[0] <= X_img and mouse[1] <= Y_img:
                players.playerList.append(players.Player(mouse[0], mouse[1], buttons.color))
            elif buttons.mode == "move":
                players.clickInMoveMode(mouse[0], mouse[1])
            elif buttons.mode == "delete":
                players.clickInDeleteMode(mouse[0], mouse[1])
    if players.selectedPlayer is not None and buttons.mode == "move":
        players.selectedPlayer.setPos(mouse[0], mouse[1])
    screen.blit(field_surface, (0, 0))
    players.render(screen)
    buttons.render(screen)
    pygame.display.flip()