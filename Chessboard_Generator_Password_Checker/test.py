
import sys
sys.setrecursionlimit(10**6)
class Password():
    def __init__(self):
        self.__password = None
        self.__message = ""
        self.__valid = True

    def isValid(self):
        self.isPassword()
        self.is123()
        self.isLongEnough()
        self.isLetter()
        self.isDigit()
        self.isSpecial()
        # self.isEnoughDigits()
        return self.isValid()

    def setPassword(self, password):
        self.__password = password

    def isPassword(self):
        word = "password"
        if word in self.__password:
            self.__message += "Cannot contain word 'password'\n"
            self.__valid = False


    def is123(self):
        string = "123"
        if string in self.__password:
            self.__message += "Cannot contain '123' in password\n"
            self.__valid = False


    def isDigit(self):
        count1 = 0
        for i in self.__password:
            if i.isdigit():
                count1 += 1
        if count1 <= 2:
            pass
        else:
            self.__message += "must contain atleast 2 digits\n"
            self.__valid = False

    def isLongEnough(self):
        if len(self.__password) > 8:
            self.__message += "must be atleast 8 characters long\n"
            self.__valid = False

    def isLetter(self):
        count = 0
        for j in self.__password:
            if j.isalpha():
                count += 1
        if count < 1:
            self.__message += "password must contain atleast 1 letter\n"
            self.__valid = False

    def isSpecial(self):
        if not self.__password.isalnum():
            self.__message += "must not contain special characters\n"
            self.__valid = False



    def getErrorMessage(self):
        if self.isValid():
            print("password accepted!")
        else:
            print(self.__message)

    def main(self):
        self.isValid()
        self.getErrorMessage()


password1 = Password()
password1.setPassword(input("Enter in a password: "))
password1.main()


