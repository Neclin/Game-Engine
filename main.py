import pygame
import time

import random

from canvas import Canvas
from renderer import Renderer, Camera
from eventManager import EventManager
from gameObject import GameObject
from playerController import Player

backgroundScale = 3

world = Canvas(1200*backgroundScale , 675*backgroundScale)
camera = Camera(0, 0, 800, 800, 100, world)
renderer = Renderer(800, 800, camera)
eventManager = EventManager()

FPS = 60

backgroundImage = pygame.image.load("background.png")
backgroundImage = pygame.transform.scale(backgroundImage, (1200*backgroundScale, 675*backgroundScale))
background = GameObject(0, 0, 1200*backgroundScale, 675*backgroundScale, sprite=backgroundImage)
renderer.gameObjects.append(background)

player = Player(0, 0, 20, 30)
renderer.gameObjects.append(player)

while eventManager.running:

    eventManager.checkEvents(renderer)

    newTime = time.time()
    if newTime - eventManager.oldTime >= 1 / FPS:
        eventManager.deltaTime = newTime - eventManager.oldTime
        eventManager.oldTime = newTime

        # print("FPS", 1/eventManager.deltaTime)

        # eventManager.checkCameraMovement(camera, newTime - eventManager.oldTime)

        camera.focus(player)
        player.checkPlayerMovement(camera, renderer, eventManager.deltaTime)

        renderer.show()
