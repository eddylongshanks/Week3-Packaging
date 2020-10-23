
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def details(self):
        return self.name + "            | " + str(self.age) + "             | "

    def __str__(self):
        return "Name: " + self.name + "\nAge: " + str(self.age) +"\n"
    
    def __repr__(self):
        return "User(name, age)"
