import random


def echo():
    random_numbers = [random.randint(1, 100) for _ in range(20)]
    with open("randNums.txt", 'w') as file:
        for number in random_numbers:
            file.write(str(number) + '\n')


def main():
    echo()
    with open("randNums.txt", 'r') as file:
        content = file.read()
        print(content)


if __name__ == '__main__':
    main()
