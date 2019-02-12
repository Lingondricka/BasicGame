import pygame


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

    def load_ship(self,screen):
        self.ship = pygame.transform.scale(self.ship, (50, 150))
        screen.blit(self.ship, (self.x, self.y))
