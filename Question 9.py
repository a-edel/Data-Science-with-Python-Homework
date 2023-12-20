import random


def main():
    num = random.randint(1, 100)
    if num < 50:
        print("You chose a number less than 50.")
    if num > 50:
        print("You chose a number more than 50.")


if __name__ == '__main__':
    main()
