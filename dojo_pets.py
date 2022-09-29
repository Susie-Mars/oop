class Pet:

    def __init__(self, name , type , tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 20

    def sleep(self):
        self.energy+=(25)
        print(f"Now I have energy! I'm seriously {self.tricks} right now!")
        return self

    def eat(self):
        self.energy+=(5)
        self.health+=10
        print("Nom nom nom! I looove to eat!")
        return self
        
    def play(self):
        self.health+=(5)
        self.energy+=(5)
        print("I'm even healthier now! I'm indestructible! Rawwwwwrrr!!!")
        return self

    def noise(self):
        print("Meoowwwwww!")
        return self

    def get_kitty_stats(self):
        print(f"My name is {self.name}! I have {self.health} health and {self.energy} energy!")
        return self

class Ninja:
    
    def  __init__(self, first_name , last_name , treats , pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats =  treats
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self):
        self.pet.play()
        print("Even though I'm a cat, I love to go for a walk!")
        return self
    
    def feed(self):
        self.pet.eat()
        print(f"Moooommm, I need some {self.pet_food} and {self.treats}!!")
        return(self)
    
    def bathe(self):
        self.pet.noise()
        print(f"I swear if you get water near me{self.first_name} {self.last_name}, I'll murder you!")
        return self



kitty = Pet("Cass", "kitty", "tweaking out")
magic = Ninja("Black", "Magic", "Greenies", "kibbles", kitty)

kitty.get_kitty_stats().play()
magic.feed().bathe()






