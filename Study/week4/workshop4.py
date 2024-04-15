# Bonus Task 1-5 - Completed
# Driver code for each task is added.

class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        if len(name) in range(2, 11) and self.name != name and " " not in name:
            self.name = name
        else:
            print(
                "Entered name is same as old name or Entered name length is not in range of 2 to 10 or Entered password contain spaces.")

    def change_pin(self, pin):
        if len(str(pin)) == 4 and pin != self.pin and " " not in str(pin):
            self.pin = pin
        else:
            print(
                "Entered pin is same as old pin or Entered pin length must be 4 or Entered password contain spaces.")

    def change_password(self, password):
        if len(password) >= 5 and self.password != password and " " not in password:
            self.password = password
        else:
            print(
                "Entered password is same as old password or Entered password length must be greater than 4 or Entered password contain spaces.")


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
        self.on_hold = False

    def account_status(self):
        if self.on_hold:
            self.on_hold = False
        else:
            self.on_hold = True

    def show_balance(self):
        print(self.name, "has an account balance of: $",
              "{:.2f}".format(self.balance))

    def withdraw(self, amount):
        if not(self.on_hold):
            if not(self.validate(amount)):
                if self.balance >= amount:
                    self.balance -= amount
                else:
                    print(
                        self.name, "does not have enough funds to withdraw. Curret balance is $", "{:.2f}".format(self.balance))
        else:
            print("Currently there is hold on the user account: ", self.name)
            return False

    def deposit(self, amount):
        if not(self.on_hold):
            if not(self.validate(amount)):
                self.balance += amount
        else:
            print("Currently there is hold on the user account: ", self.name)
            return False

    def transfer_money(self, userTo, amount):
        if not(self.on_hold):
            if self.validate(amount):
                return False
            print("\nYou are transferring $", amount, "to", userTo.name)
            print("Authentcation required")
            pinOfTranUser = input(
                "Enter pin of transfer the amount: ")
            if pinOfTranUser == str(self.pin):
                if self.balance >= amount:
                    print("Transfer Authorized")
                    print("Transferring $", amount, "to", userTo.name)
                    self.balance -= amount
                    userTo.balance += amount
                    return True
                else:
                    print(
                        self.name, "does not have enough funds to transfer. Curret balance is $", "{:.2f}".format(self.balance))
                    return False
            else:
                print("Incorrect pin")
                return False
        else:
            print("Currently there is hold on the user account: ", self.name)
            return False

    def request_money(self, userFrom, amount):
        if not(self.on_hold):
            if self.validate(amount):
                return False
            print("\nYou are reequesting $", amount, "from", userFrom.name)
            print("User Authentication required!")
            pinofFromUser = input(
                "Enter pin of the user you requesting money from: ")
            if str(userFrom.pin) == pinofFromUser:
                userPassword = input(
                    "Enter password of the user requesting money:")
                if userPassword == self.password:
                    if userFrom.balance >= amount:
                        print("Request Authorized")
                        print(userFrom.name, "sent $", amount)
                        userFrom.balance -= amount
                        self.balance += amount
                        return True
                    else:
                        print(
                            userFrom.name, "does not have enough funds to transfer. Curret balance is $", "{:.2f}".format(userFrom.balance))
                        return False
                else:
                    print("Password entered is incorrect")
                    return False
            else:
                print("PIN entered is incorrect")
                return False
        else:
            print("Currently there is hold on the user account: ", self.name)
            return False

    def validate(self, amount):
        if not(str(amount).isnumeric()) or not(amount > 0):
            print("Entered amount need to be whole number and greater than 0")
            return True
        return False


""" Driver Code for Task 1 """
#user1 = User("Bob", 1234, "password")
#print(user1.name, user1.pin, user1.password)

""" Driver Code for Task 2 """
#user1 = User("Bob", 1234, "password")
#print(user1.name, user1.pin, user1.password)
# user1.change_name("Bobby")
# user1.change_pin(4321)
# user1.change_password("newpassword")
#print(user1.name, user1.pin, user1.password)

""" Driver Code for Task 3"""
#bankUser1 = BankUser("Bob", 1234, "password")
#print(bankUser1.name, bankUser1.pin, bankUser1.password, bankUser1.balance)

""" Driver Code for Task 4"""
#bankUser1 = BankUser("Bob", 1234, "password")
# bankUser1.show_balance()
# bankUser1.deposit(1000)
# bankUser1.show_balance()
# bankUser1.withdraw(500)
# bankUser1.show_balance()

""" Driver Code for Task 5"""
#bankUser1 = BankUser("Bob", 1234, "bpassword")
#bankUser2 = BankUser("Alice", 4321, "apassword")
# bankUser2.deposit(5000)
# bankUser1.show_balance()
# bankUser2.show_balance()
#bankUser2.transfer_money(bankUser1, 500)
# bankUser1.show_balance()
# bankUser2.show_balance()
#bankUser2.request_money(bankUser1, 250)
# bankUser1.show_balance()
# bankUser2.show_balance()

""" Driver Code for Bonus Task 1"""
#bankUser1 = BankUser("Bob", 1234, "bpassword")
#bankUser2 = BankUser("Alice", 4321, "apassword")
# bankUser2.deposit(5000)
# bankUser2.deposit(-5000)
# bankUser2.withdraw(-5000)
#bankUser2.transfer_money(bankUser1, -500)
#bankUser2.request_money(bankUser1, -500)

""" Driver Code for Bonus Task 2"""
#bankUser1 = BankUser("Bob", 1234, "bpassword")
#bankUser2 = BankUser("Alice", 4321, "apassword")
# bankUser2.deposit(1000)
# bankUser1.deposit(500)
#bankUser2.transfer_money(bankUser1, 2000)
#bankUser1.request_money(bankUser2, 1001)

""" Driver Code for Bonus Task 3"""
#bankUser1 = BankUser("Bob", 1234, "bpassword")
# bankUser1.change_name("Bob")
# bankUser1.change_name("B")
# bankUser1.change_name("12345678901")
#bankUser1.change_name("B o b1")
# print("\n")
# bankUser1.change_password("bpassword")
# bankUser1.change_password("1234")
#bankUser1.change_password(" 12345")
# print("\n")
# bankUser1.change_pin(1234)
# bankUser1.change_pin(1)
# bankUser1.change_pin(12345)

""" Driver Code for Bonus Task 4"""
#bankUser1 = BankUser("Bob", 1234, "bpassword")
# bankUser1.deposit(100)
# bankUser1.show_balance()

""" Driver Code for Bonus Task 5"""
#bankUser1 = BankUser("Bob", 1234, "bpassword")
# bankUser1.account_status()
# bankUser1.deposit(1000)
# bankUser1.withdraw(1000)
# bankUser1.account_status()
# bankUser1.deposit(1000)
# bankUser1.show_balance()
# bankUser1.withdraw(1000)
# bankUser1.show_balance()
