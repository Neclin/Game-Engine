import pygame
import time

import random

from renderer import Renderer, Camera
from eventManager import EventManager
from gameObject import GameObject

camera = Camera(200, 200, 400, 400, 100)
renderer = Renderer(800, 800, camera)
eventManager = EventManager()

FPS = 60

player = GameObject(100, 100, 50, 50)
renderer.gameObjects.append(player)

while eventManager.running:

    eventManager.checkEvents()

    newTime = time.time()
    if newTime - eventManager.oldTime >= 1 / FPS:
        eventManager.deltaTime = newTime - eventManager.oldTime
        eventManager.oldTime = newTime

        print("FPS", 1/eventManager.deltaTime)

        eventManager.checkEvents()
        # eventManager.checkCameraMovement(camera, newTime - eventManager.oldTime)

        eventManager.checkPlayerMovement(player, camera, eventManager.deltaTime)
        camera.focus(player)

        renderer.show()
