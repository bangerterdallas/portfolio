from password import Password

def main():
    # Tell the user what the password parameters are
    print("Password must be 8 characters long")
    print("Password must contain at least one letter and at least two numbers")
    print("Password cannot have any special characters")

    # Create a loop until the user enters a password that satisfies the parameters
    loop = True
    while loop:
        # ask the user for the desired password
        userPassword = input("Enter the desired password: ")

        # Run the class
        password = Password()
        password.setPassword(userPassword)
        password.isValid()
        password.getErrorMessage()

        #Break the loop if password meets required parameters
        if password.getErrorMessage() == "":
            loop = False
    print("Password meets parameters")

main()
