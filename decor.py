from pygame import Vector2, Vector3, Surface
import pygame

class Roof():
    def __init__(self,
                 bottomLeftPos : Vector2,
                 height : int,
                 width : int,
                 color : Vector3) -> None:
        self.bottomLeftPos = bottomLeftPos
        self.height = height
        self.width = width
        self.color = color

    def draw(self, screen : Surface) -> None:
        pass

class FlatRoof(Roof):
    def draw(self, screen : Surface) -> None:
        pygame.draw.rect(screen, self.color, (self.bottomLeftPos.x, self.bottomLeftPos.y,self.width, self.height))

class SlopedRoof(Roof):
    def draw(self, screen : Surface) -> None:
        rightX = int(self.bottomLeftPos.x) + self.width - 1
        topY = int(self.bottomLeftPos.y) - self.height
        pygame.draw.polygon(screen, self.color, [(self.bottomLeftPos), (rightX, self.bottomLeftPos.y), (rightX, topY)])

class SpikedRoof(Roof):
    def draw(self, screen: Surface) -> None:
        tierHeight = self.height * .1

        pygame.draw.rect(screen, self.color, (self.bottomLeftPos.x, self.bottomLeftPos.y,self.width, tierHeight))
        pygame.draw.rect(screen, self.color, (self.bottomLeftPos.x + (self.width * .1), self.bottomLeftPos.y - tierHeight,self.width*.8, tierHeight * 1))
        pygame.draw.rect(screen, self.color, (self.bottomLeftPos.x + (self.width * .2), self.bottomLeftPos.y - tierHeight * 3,self.width*.6, tierHeight * 2))
        pygame.draw.rect(screen, self.color, (self.bottomLeftPos.x + (self.width * (.93/2)), self.bottomLeftPos.y - tierHeight * 8,self.width*.07, tierHeight * 5))