import random
class DiceSimulator:
    def roll_dice(self):
        number = random.randint(1, 6)
        print("Dice rolled:", number)
    def play(self):
        while True:
            self.roll_dice()
            choice = input("Roll again? (yes/no): ")
            if choice.lower() != "yes":
                print("Thank you for playing!")
                break
dice = DiceSimulator()
dice.play()

