# Minecraft Starter Game

import random
import time

class Game:
    def __init__(self):
        self.player_health = 100
        self.enemies = ['Zombie', 'Skeleton']
        self.enemy_health = 30

    def start_game(self):
        print("Welcome to the Minecraft Starter Game!")
        while self.player_health > 0:
            enemy = random.choice(self.enemies)
            print(f"A wild {enemy} appeared!")
            self.battle(enemy)
        print("Game Over!")

    def battle(self, enemy):
        while self.enemy_health > 0 and self.player_health > 0:
            action = input("Choose your action (attack/run): ").lower()
            if action == "attack":
                damage = random.randint(5, 15)
                print(f"You dealt {damage} damage to the {enemy}.")
                self.enemy_health -= damage
                if self.enemy_health <= 0:
                    print(f"You defeated the {enemy}!")
                    self.enemy_health = 30  # Reset enemy health
                    break
                enemy_damage = random.randint(1, 10)
                print(f"{enemy} dealt {enemy_damage} damage to you.")
                self.player_health -= enemy_damage
                print(f"Your health: {self.player_health}")
            elif action == "run":
                print("You ran away!")
                break
            else:
                print("Invalid action!")
        print(f"Remaining health: {self.player_health}")

if __name__ == '__main__':
    game = Game()
    game.start_game()