import pygame

from gameObject import GameObject

class Player(GameObject):
    def __init__(self, x, y, width, height, sprite=None):
        super().__init__(x, y, width, height, sprite=sprite)

        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = 250



    def checkPlayerMovement(self, camera, renderer, deltaTime):
        print(self.velocity)
        keys = pygame.key.get_pressed()

        step = self.acceleration * deltaTime

        if keys[pygame.K_w]:
            self.velocity.y -= step
        if keys[pygame.K_s]:
            self.velocity.y += step
        if keys[pygame.K_a]:
            self.velocity.x -= step
        if keys[pygame.K_d]:
            self.velocity.x += step
        
        self.velocity *= 0.9

        self.playerMovement(renderer, deltaTime)

    def playerMovement(self, renderer, deltaTime):
        
        newPosition = self.worldPosition + self.velocity * 5 * deltaTime

        for gameObject in renderer.gameObjects:
            if gameObject.type == "hitbox":
                newRect = pygame.Rect(newPosition.x, newPosition.y, self.width, self.height)
                if gameObject.rect.colliderect(newRect):
                    return

        self.worldPosition = newPosition