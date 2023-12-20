def delta():
    age = -1
    while not(0 <= age <= 100):
        age = int(input("What is your age? "))
    return age


def main():
    age = delta()
    print("Your age is: " + str(age))


if __name__ == '__main__':
    main()
