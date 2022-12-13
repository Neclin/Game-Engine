import pygame

class GameObject():
    def __init__(self, x, y, width, height, sprite=None):
        self.worldPosition = pygame.Vector2(x, y)
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)

        self.sprite = sprite

        self.velocity = 200

    def show(self, win, camera):
        if self.sprite:
            print(camera.worldPosition)
            win.blit(self.sprite, self.worldPosition - camera.worldPosition)
        else:
            self.rect = pygame.Rect(camera.position.x + self.worldPosition.x - camera.worldPosition.x, 
                                    camera.position.y + self.worldPosition.y - camera.worldPosition.y, 
                                    self.width, self.height)
            pygame.draw.rect(win, (255, 255, 255), self.rect)