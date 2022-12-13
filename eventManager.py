import pygame
import time

class EventManager():
    def __init__(self):
        self.running = True

        self.oldTime = time.time()
        self.deltaTime = 0

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

    def checkCameraMovement(self, camera, deltaTime):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            camera.worldPosition.y -= camera.velocity * deltaTime
        if keys[pygame.K_s]:
            camera.worldPosition.y += camera.velocity * deltaTime
        if keys[pygame.K_a]:
            camera.worldPosition.x -= camera.velocity * deltaTime
        if keys[pygame.K_d]:
            camera.worldPosition.x += camera.velocity * deltaTime

    def checkPlayerMovement(self, player, camera, deltaTime):
        keys = pygame.key.get_pressed()

        step = player.velocity * deltaTime
        if keys[pygame.K_w] and player.worldPosition.y - step > 0:
            player.worldPosition.y -= step
        if keys[pygame.K_s] and player.worldPosition.y + step < camera.worldWidth - player.height:
            player.worldPosition.y += step
        if keys[pygame.K_a] and player.worldPosition.x - step > 0:
            player.worldPosition.x -= step
        if keys[pygame.K_d] and player.worldPosition.x + step < camera.worldHeight - player.width:
            player.worldPosition.x += step