from account import Account


def main():
    loop = True
    while loop:
        i_d = input("Enter your ID, or press ENTER: ")
        if i_d == "":
            break
        elif float(i_d) < 0:
            print("Enter a positive number")
        else:
            break
    loop = True
    while loop:
        balance = input("Enter your bank balance, or press ENTER: ")
        if balance == "":
            break
        elif float(balance) < 0:
            print("Enter a positive number")
        else:
            break
    loop = True
    while loop:
        annual_interest_rate = input("Enter the Annual Interest Rate, or press ENTER: ")
        if annual_interest_rate == "":
            break
        elif float(annual_interest_rate) < 0:
            print("Enter a positive number")
        elif float(annual_interest_rate) > 10:
            print("Enter a percent less than 10")
        else:
            break
    account1 = Account(i_d, balance, annual_interest_rate)
    account1.set_id()
    account1.set_balance()
    account1.set_annual_interest_rate()
    play_again = True
    while play_again:
        account1.get_display()
        menu_choice = eval(input("Choose a category: "))
        if menu_choice == 1:
            account1.get_id()
        elif menu_choice == 2:
            account1.get_balance_string()
        elif menu_choice == 3:
            account1.get_annual_interest_rate()
        elif menu_choice == 4:
            account1.get_monthly_interest_rate()
        elif menu_choice == 5:
            account1.get_monthly_interest()
        elif menu_choice == 6:
            loop = True
            while loop:
                withdraw_money = float(input("Enter the amount you wish to withdraw: "))
                if float(withdraw_money) < 0:
                    print("Enter a valid number that is not negative")
                elif withdraw_money > account1.get_balance():
                    print("That withdrawal exceeds your funds")
                else:
                    break
            account1.withdraw(withdraw_money)
        elif menu_choice == 7:
            loop = True
            while loop:
                deposit_money = float(input("Enter the amount you wish to deposit: "))
                if float(deposit_money) < 0:
                    print("Enter a valid number that is not negative")
                else:
                    break
            account1.deposit(deposit_money)
        else:
            print("Thanks")
            break


main()