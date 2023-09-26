from controller.users import Users
# db= HandleDB()
data = {"firstname":"Raul","lastname":"Martinez","username":"rimartinez","country":"co","password_user":"1234" }
users = Users(data)
users.create_user()


