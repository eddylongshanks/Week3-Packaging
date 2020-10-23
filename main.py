import UserList.users as UserList
from Users.admin import Admin
from Users.user import User

users = UserList.Users()
numberOfUsers = int(input("How many users?: "))

while numberOfUsers > 0:
    name = input("What is the name?: ")
    age = input("What is the age?: ")
    currentUser = User(name, age)
    users.AddUser(currentUser)
    numberOfUsers -= 1

admin = Admin("Chris", 30)
users.AddUser(admin)

users.GetUsers()
