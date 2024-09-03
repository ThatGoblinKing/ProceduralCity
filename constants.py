class GameWindow:
    FPS : int = 60
    SCREEN : tuple[int,int] = (1920, 1080)
    BACKGROUND_COLOR : tuple[int,int,int] = (0,0,0)

class BuildingDefaults:
    COLOR = (100,100,100)
    HEIGHT = 600
    WIDTH = 200
    POS = (GameWindow.SCREEN[0]//2 - WIDTH//2, GameWindow.SCREEN[1] - HEIGHT)
    ROOF_STYLE = 0
    WINDOW_STYLE = 0

class RoofStyles:
    FLAT = 0
    SLOPE = 1
    SPIKE = 2

class Generation:
    BUIDLING_COUNT = 80
    DARKEST_VALUE = 90
    LIGHTEST_VALUE = 179