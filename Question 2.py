def main():
    chances = 1
    name = input("What is your name? ")
    while not chances == 3 and not name.isalpha():
        name = input("Invalid name. What is your name? ")
        chances += 1
    age = int(input("What is your age? "))
    while not chances == 3 and not 1 <= age <= 100:
        age = input("Invalid age.What is your age? ")
        chances += 1
    if chances == 3:
        print("Unacceptable")
    else:
        print("Acceptable")


if __name__ == '__main__':
    main()
