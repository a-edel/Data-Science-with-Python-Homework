import string


def main():
    valid = False
    while valid is False:
        valid = True
        password = input("What is your password? (Valid passwords must contain 8 or more characters," +
                         " a number, an uppercase letter, a lowercase letter, and a special character? ")
        if len(password) < 8:
            print("Password should be at least 8 characters long.")
            valid = False
        if not any(char.isdigit() for char in password):
            print("Password should contain a number.")
            valid = False
        if not any(char.isupper() for char in password):
            print("Password should contain an uppercase letter.")
            valid = False
        if not any(char.islower() for char in password):
            print("Password should contain a lowercase letter.")
            valid = False
        if not any(char in string.punctuation for char in password):
            print("Password should contain a special character.")
            valid = False


if __name__ == '__main__':
    main()
