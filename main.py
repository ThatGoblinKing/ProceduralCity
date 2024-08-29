import pygame
from building import Building
from constants import GameWindow, RoofStyles

pygame.init

screen = pygame.display.set_mode(GameWindow.SCREEN)

doExit = False
clock = pygame.time.Clock()

testBuilding = Building(roofStyle=RoofStyles.SPIKE)

while not doExit:
    delta = clock.tick(GameWindow.FPS)/1000
    screen.fill(GameWindow.BACKGROUND_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True

    testBuilding.draw(screen)

    pygame.display.flip()
pygame.quit()