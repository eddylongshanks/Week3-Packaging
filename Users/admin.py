from Users.user import User

# Inherit from User
class Admin(User):
    def details(self):
        return self.name + " (Admin) | " + str(self.age) + "             | "

    # __str__ will return this line when calling the class. eg: print(user1)
    def __str__(self):
        return "Name: " + self.name + " (Admin)\nAge: " + str(self.age) +"\n"
    
    def __repr__(self):
        return "Admin(User)"