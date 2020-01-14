class Password:
    #Create constructor
    def __init__(self):
        self.__password = None
        self.message = ""
        self.valid = False

    # Create useless method to set the password
    def setPassword(self, userPassword):
        self.__password = userPassword

    # Create method to check the length to be used later in isValid
    def passwordLength(self):
        if len(self.__password) < 8:
            self.message += "Password is too short\n "

    # Create method to check integer count to be used later in isValid
    def containsTwoInts(self):
        count = 0
        for s in self.__password:
            if s.isdigit():
                count += 1
        if count <= 1:
            self.message += "Password does not contain more than two numbers.\n "

    # Create method to check letter count to be used later in isValid
    def containsLetter(self):
        count = 0
        for s in self.__password:
            if s.isalpha():
                count += 1
        if count < 1:
            self.message += "Password does not contain any letters\n "

    # Create method to check special characters to be used later in isValid
    def specialCharacter(self):
        if str.isalnum(self.__password) == False:
            self.message += "Password contains a special character\n "

    #Create method to check if password has 123
    def is123(self):
        string = "123"
        if string in self.__password:
            self.message += "Cannot contain '123' in password\n"


        # check if the password is valid
    def isValid(self):
        for i in range(1):
            # check the length of the password
            self.passwordLength()

            # Check to see if it contains at least two numbers
            self.containsTwoInts()

            # Check to see if it contains at least one letter
            self.containsLetter()

            # Check to see if it contains any special characters
            self.specialCharacter()

            # Check to see if it contains the string "123"
            self.is123()

            # If the message is blank the password is correct so the password is valid (True)
            if self.message == "":
                return True
            else:
                return False

    # Print the error messages telling the user what is wrong with their password
    def getErrorMessage(self):
        if self.isValid() == True:
            return ""
        elif self.isValid() == False:
            return print(self.message)
