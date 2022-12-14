import pygame

class Renderer():
    def __init__(self, screenWidth, screenHeight, camera):
        self.win = pygame.display.set_mode((screenWidth, screenHeight))

        self.camera = camera

        self.gameObjects = []

        self.hitboxPos1 = None

    def show(self):
        self.win.fill((51,51,51))

        # draw the outline of the camera
        pygame.draw.rect(self.win, (0, 0, 0), self.camera.rect, 1)

        for gameObject in self.gameObjects:
            if (gameObject.worldPosition.x + gameObject.width >= self.camera.worldPosition.x 
            and gameObject.worldPosition.x <= self.camera.worldPosition.x + self.camera.width 
            and gameObject.worldPosition.y + gameObject.height >= self.camera.worldPosition.y 
            and gameObject.worldPosition.y <= self.camera.worldPosition.y + self.camera.height):
                gameObject.show(self.win, self.camera)

        if self.hitboxPos1:
            mousePos = pygame.mouse.get_pos()
            pygame.draw.rect(self.win, (0, 0, 0), pygame.Rect(self.hitboxPos1, (mousePos[0] - self.hitboxPos1[0], mousePos[1] - self.hitboxPos1[1])), 1)

        pygame.display.update()

class Camera():
    def __init__(self, x, y, width, height, velocity, world):
        self.position = pygame.Vector2(x, y)
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)

        self.worldPosition = pygame.Vector2(0, 0)
        self.velocity = velocity

        self.world = world


    def focus(self, gameObject):
        gameObjectMiddle = pygame.Vector2(gameObject.worldPosition.x + gameObject.width / 2, gameObject.worldPosition.y + gameObject.height / 2)
        self.worldPosition = pygame.Vector2(gameObjectMiddle.x - self.width / 2, gameObjectMiddle.y - self.height / 2)

        self.worldPosition.x = max(0, self.worldPosition.x)
        self.worldPosition.y = max(0, self.worldPosition.y)

        self.worldPosition.x = min(self.worldPosition.x, self.world.width - self.width)
        self.worldPosition.y = min(self.worldPosition.y, self.world.height - self.height)