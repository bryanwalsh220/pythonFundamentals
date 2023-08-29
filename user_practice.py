
class User:
    def __init__(self, first, last, email, age):
        self.first = first
        self.last = last
        self.email = email
        self.age = age
        self.rewards = False
        self.gold = 0


    def display_info(self):
        print(f"First Name: {self.first}")
        print(f"Last Name: {self.last}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Memeber?: {'Yes' if self.rewards else 'No'}")
        print(f"Gold Card Points: {self.gold}")
        return self
    
    def enroll(self):
        if self.rewards:
            print("You're already a member")
        else:
            self.rewards = True
            self.gold = 200
        return self
        
    
    def spend_points(self,amount):
        if amount > self.gold:
            print("Not enough points")
        else:
            self.gold -= amount
            print(f'You have {self.gold} points remaining')
        return self




Bryan = User('Bryan', 'Walsh', 'email.com', 29)
Bryan.display_info().enroll().display_info().spend_points(50).display_info().spend_points(250).display_info()
