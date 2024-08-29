from constants import BuildingDefaults as default, RoofStyles
from pygame import Vector3, Vector2, Rect, Surface
from decor import *
import pygame

class Building:
    def __init__(self,
                 color : Vector3=Vector3(default.COLOR),
                 height : int=default.HEIGHT,
                 width : int=default.WIDTH,
                 pos : Vector2 = Vector2(default.POS),
                 roofStyle : int = default.ROOF_STYLE,
                 windowStyle : int = default.WINDOW_STYLE
                 ) -> None:
        self.rect = Rect(pos.x, pos.y, width, height)
        self.color = color
        self.roof : Roof = self.createRoof(roofStyle)
        self.windows : list[Rect]

    def createRoof(self, roofStyle : int) -> Roof | None:
        if roofStyle == RoofStyles.FLAT:
            return FlatRoof(Vector2(self.rect.topleft), self.rect.height * .01, self.rect.width, self.color)
        elif roofStyle == RoofStyles.SLOPE:
            return SlopedRoof(Vector2(self.rect.topleft), self.rect.height * .25, self.rect.width, self.color)
        elif roofStyle == RoofStyles.SPIKE:
            return SpikedRoof(Vector2(self.rect.topleft), self.rect.height * .5, self.rect.width, self.color)

    def draw(self, screen : Surface):
        pygame.draw.rect(screen, self.color, self.rect)
        self.roof.draw(screen)