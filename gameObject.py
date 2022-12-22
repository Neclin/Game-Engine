import pygame

class GameObject():
    def __init__(self, x, y, width, height, 
    colidable=False,
    sprite=None, type="GameObject"):
        self.worldPosition = pygame.Vector2(x, y)
        self.width = width
        self.height = height

        if width < 0:
            self.width *= -1
            self.worldPosition.x -= self.width
        
        if height < 0:
            self.height *= -1
            self.worldPosition.y -= self.height

        self.rect = pygame.Rect(x, y, width, height)

        self.collidable = colidable
        if self.collidable:
            self.hitbox = pygame.Rect(x, y, width, height)

        self.sprite = sprite

        self.type = type

        self.velocity = 200

    def show(self, win, camera):
        if self.sprite:
            win.blit(self.sprite, camera.position + self.worldPosition - camera.worldPosition)
        else:
            self.border = pygame.Rect(camera.position.x + self.worldPosition.x - camera.worldPosition.x - 1,
                                    camera.position.y + self.worldPosition.y - camera.worldPosition.y - 1,
                                    self.width + 2, self.height + 2)
            pygame.draw.rect(win, (0, 0, 0), self.border, 1)

            if self.type == "hitbox":
                return

            self.rect = pygame.Rect(camera.position.x + self.worldPosition.x - camera.worldPosition.x, 
                                    camera.position.y + self.worldPosition.y - camera.worldPosition.y, 
                                    self.width, self.height)
            pygame.draw.rect(win, (255, 255, 255), self.rect)