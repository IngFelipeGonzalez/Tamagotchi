class Tamagotchi:
    def __init__(self):
        self.sleep = 8000
        self.hunger = 0
        self.happiness = 0

    def sleep_prog(self):
        self.sleep += 500

    def feed(self, food_option):
        print(food_option)
        if food_option == "Hamburguer":
            self.hunger -= 20
        elif food_option == "Cake":
            self.hunger -= 5
        else:
            self.hunger -= 10

    def play(self):
        self.happiness += 10

    def update(self):
        self.hunger += 1
        self.happiness -= 1
        self.sleep -= 100

    def get_status(self):
        return (
            f"Hunger: {self.hunger}\nHappiness: {self.happiness}\nEnergy: {self.sleep}"
        )
