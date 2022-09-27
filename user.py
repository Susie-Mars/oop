
class User:
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.age = data['age']
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"{self.first_name}, {self.last_name}, {self.email}, {self.age}, {self.is_rewards_member}, {self.gold_card_points}")
        return self

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self
    
    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points * (1.00 - amount)
        return self
    

        
user= User({
    'first_name': 'Susie',
    'last_name': 'Mars',
    'email': 'susie@mail.com',
    'age': '37'
})
user2= User({
    'first_name': 'Steve',
    'last_name': 'Tobias',
    'email': 'steve@mail.com',
    'age': '28'
})
user3= User({
    'first_name': 'Sally',
    'last_name': 'Jones',
    'email': 'sally@mail.com',
    'age': '42'
})

user.enroll()
user2.enroll()

user2.spend_points(.4)

user.display_info()
user2.display_info()
user3.display_info()






