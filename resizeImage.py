import pygame

image = pygame.image.load("background.png")

image = pygame.transform.scale(image, (1200*3, 675*3))

pygame.image.save(image, "backgroundScaled.png")