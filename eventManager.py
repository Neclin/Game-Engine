import pygame
import time

from gameObject import GameObject

class EventManager():
    def __init__(self):
        self.running = True

        self.oldTime = time.time()
        self.deltaTime = 0

        self.pos1 = None

    def checkEvents(self, renderer):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousePosition = pygame.mouse.get_pos()
                mousePosition = pygame.Vector2(mousePosition[0], mousePosition[1])

                if event.button == 1:
                    if not renderer.hitboxPos1:
                        renderer.hitboxPos1 = mousePosition
                    else:
                        pos = renderer.hitboxPos1 + renderer.camera.worldPosition
                        worldMousePosition = mousePosition + renderer.camera.worldPosition
                        hitbox = GameObject(pos.x, pos.y, worldMousePosition.x - pos.x, worldMousePosition.y - pos.y, type="hitbox")
                        renderer.gameObjects.append(hitbox)
                        renderer.hitboxPos1 = None


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