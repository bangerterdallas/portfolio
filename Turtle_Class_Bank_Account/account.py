# Create the class
class Account:
    # Create constructor
    def __init__(self, i_d, balance, annual_interest_rate):
        self.__id = i_d
        self.__balance = balance
        self.__annual_interest_rate = annual_interest_rate

    # Create a method to display the display so the user can interact with it
    @staticmethod
    def get_display():
        display = "(1):Display ID \n (2):Display Balance \n (3): Display Annual Interest Rate \n"
        display2 = "(4): Display Monthly Interest Rate \n (5): Display Monthly Interest \n"
        display3 = "(6): Withdraw Money \n (7): Deposit Money \n (8): Exit"
        return print(display, display2, display3)

    # Create default id/id setter
    def set_id(self):
        if self.__id == "":
            self.__id = 0
        else:
            self.__id = float(self.__id)

    # 1
    # Create get and set ID method
    def get_id(self):
        return print(str(self.__id) + " is your ID")

    def set_balance(self):
        if self.__balance == "":
            self.__balance = 100
        else:
            self.__balance = float(self.__balance)

    # 2
    # Create a get and set balance method
    def get_balance_string(self):
        return print(str(self.__balance) + "$ is your balance")

    def get_balance(self):
        return self.__balance

    # 3
    # Create a set annual interest set and get method
    def set_annual_interest_rate(self):
        # Default parameters
        if self.__annual_interest_rate == "":
            self.__annual_interest_rate = 0
            # Correctly create an annual interest rate percentage
        else:
            self.__annual_interest_rate = float(self.__annual_interest_rate)
        self.__annual_interest_rate = self.__annual_interest_rate / 100

    def get_annual_interest_rate(self):
        return print(str(self.__annual_interest_rate) + " is your annual interest rate")

    # 4
    # Create a get monthly interest method
    def get_monthly_interest_rate(self):
        monthly_interest_rate = self.__annual_interest_rate / 12
        return print(str(monthly_interest_rate) + " is your monthly interest rate")

    # 5
    # Create get monthly interest amount method
    def get_monthly_interest(self):
        monthly_interest_rate = self.__annual_interest_rate / 12
        monthly_interest = self.__balance * monthly_interest_rate
        return print(str(monthly_interest) + "$ is your monthly interest")

    # 6
    # Create a withdraw method to take away money from the balance object
    def withdraw(self, withdraw_money):
        self.__balance -= withdraw_money
        return print(str(withdraw_money) + "$ has been removed from your account")

    # 7
    # Create method to put money into the balance object
    def deposit(self, deposit_money):
        self.__balance += deposit_money
        return print(str(deposit_money) + "$ has been added to your account")
