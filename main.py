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



class Game:
    def __init__(self):
        self.player = Hero("Player", 100, 10)
        self.computer = Hero("Computer", 100, 10)

    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            print(f"{self.player.name} attacks {self.computer.name}!")
            if not self.computer.is_alive():
                print(f"{self.player.name} wins!")
                break

            self.computer.attack(self.player)
            print(f"{self.computer.name} attacks {self.player.name}!")
            if not self.player.is_alive():
                print(f"{self.computer.name} wins!")
                break

        if __name__ == "__main__":
            game = Game()
            game.start()
