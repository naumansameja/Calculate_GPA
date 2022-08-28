class ATM_user:
    users = []

    def add_user(self, username, password, balance=0):
        user = ATM(username, password, balance)
        ATM.users.append(user)

    def get_balance(self, username):
        for user in ATM_user.users:
            if user.user_name == username:
                return user.balance
        print("User does not exist")

    def remove_user(self, username):
        for user in ATM_user.users:
            if user.user_name == username:
                ATM_user.users.remove(user)
                return
        print("User does not exist")


    def increase_balance(self, username, inc):
        for user in ATM_user.users:
            if user.user_name == username:
                user.balance += inc
                return
        print("User does not exist")

    def withdraw(self, username, password, amount):
        for user in ATM_user.users:
            if user.user_name == username:
                if amount > user.balance:
                    raise Exception("Low Balance")
                if password == user.password:
                    user.balance -= amount
                    print("Transaction successful")
                else:
                    raise Exception("Invalid username or password")
                return
        print("User does not exist")


class ATM(ATM_user):
    def __init__(self, username, password, balance=0):
        self.user_name = username
        self.password = password
        self.balance = balance


admin = ATM_user()
admin.add_user("nauman.sameja", "abc")
admin.increase_balance("nauman.sameja", 5000)
admin.withdraw("nauman.sameja", "abc", 3000)
print(admin.get_balance("nauman.sameja"))