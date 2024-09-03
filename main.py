import pygame
from pygame import Vector2
from building import Building
from constants import GameWindow, RoofStyles, Generation
import random

pygame.init

screen = pygame.display.set_mode(GameWindow.SCREEN)

doExit = False
clock = pygame.time.Clock()

testBuilding = Building(roofStyle=RoofStyles.FLAT)

while not doExit:
    delta = clock.tick(GameWindow.FPS)/1000
    screen.fill(GameWindow.BACKGROUND_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True

    for i in range(Generation.BUIDLING_COUNT):
        value = random.randint(Generation.DARKEST_VALUE, Generation.LIGHTEST_VALUE)

    pygame.display.flip()
pygame.quit()