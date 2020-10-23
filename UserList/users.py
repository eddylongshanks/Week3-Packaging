from Users.admin import Admin
from Users.user import User

class Users:
    def __init__(self):
        self.users = []
    
    def AddUser(self, user):
        # Check for the type of the object to determine admin status
        if user is type(Admin):
            user = Admin(user.name, user.age)
        elif user is type(User):
            user = User(user.name, user.age)
        self.users.append(user)
    
    def GetUsers(self):        
        print("\nThere are {0} users\n".format(str(len(self.users))))
        print("Name         | Age           | ")
        for user in self.users:            
            print(user.details())
    
    def __str__(self):
        return "There are {0} users\n".format(str(len(self.users)))

    def __repr__(self):
        return "Users()"
