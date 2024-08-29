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
        pygame.draw.rect(screen, (255,255,255), (self.bottomLeftPos.x + (self.width - (self.width * .4) * 1.75), self.bottomLeftPos.y - tierHeight * 2,self.width*.4, tierHeight * 2))
