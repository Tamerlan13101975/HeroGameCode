import pygame
pygame.init()


class Hero:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        target.health -= self.attack_power

    def is_alive(self):
        return self.health > 0





