import pygame
from pygame.locals import *

pygame.init()

display_width = 800
display_height = 600


class Battleship:
    x = 400
    y = 450
    image = "ship.png"
    ship = pygame.image.load(image)
    def _init_(self):
        self.name = "Galactica"
        self.x = 400
        self.y = 450
        self.image = "ship.png"
        self.ship = pygame.image.load("ship.png")

    def load_ship(self):
        shipboi.ship = pygame.transform.scale(shipboi.ship, (50, 150))
        screen.blit(self.ship, (shipboi.x, shipboi.y))


screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Ship boi')
white = [255, 255, 255]
red = [255, 0, 0]
screen.fill(red)
shipboi = Battleship()
shipboi.load_ship()

#shipboi.ship = pygame.transform.scale(shipboi.ship,(50,150))
#screen.blit(shipboi.ship, (shipboi.x, shipboi.y))


def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT or (
                event.type == KEYDOWN and (
                event.key == K_ESCAPE or
                event.key == K_q
        )):
            pygame.quit()
            quit()


def backgroundChanger(i):
    screen.fill([i, 0, 0])
    print(i)


def ship_controller():
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        screen.fill(red)
        shipboi.x = shipboi.x - 10
        screen.blit(shipboi.ship, (shipboi.x, shipboi.y))
    if keys[K_RIGHT]:
        screen.fill(red)
        shipboi.x = shipboi.x + 10
        screen.blit(shipboi.ship,(shipboi.x,shipboi.y))
    if keys[K_UP]:
        screen.fill(red)
        shipboi.y = shipboi.y - 10
        screen.blit(shipboi.ship, (shipboi.x, shipboi.y))
    if keys[K_DOWN]:
        screen.fill(red)
        shipboi.y = shipboi.y + 10
        screen.blit(shipboi.ship, (shipboi.x, shipboi.y))


while True:
    event_handler()
    ship_controller()
    pygame.display.update()

