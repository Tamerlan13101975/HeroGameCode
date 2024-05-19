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
        self.interface_settings = {
            'font_size': 12,
            'color_scheme': 'light',
            'controls': {'up': 'W', 'down': 'S', 'left': 'A', 'right': 'D'}
        }

        def update_interface_settings(self, setting, value):
            if setting in self.interface_settings:
                self.interface_settings[setting] = value
                print(f"Interface setting '{setting}' has been updated to '{value}'")
            else:
                print(f"Interface setting '{setting}' does not exist")

        def display_interface_settings(self):
            print("Current interface settings:")
            for key, value in self.interface_settings.items():
                print(f"{key}: {value}")

        def start(self):
            print("Игра начинается!")
            while self.player.is_alive() and self.computer.is_alive():
                self.player.attack(self.computer)
                if not self.computer.is_alive():
                    print(f"{self.player.name} побеждает!")
                    break
                self.computer.attack(self.player)
                if not self.player.is_alive():
                    print(f"{self.computer.name} побеждает!")
                    break
            print("Игра окончена.")


# Создание экземпляров героев
player = Hero("Игрок", 100, 12)
computer = Hero("Компьютер", 120, 10)

