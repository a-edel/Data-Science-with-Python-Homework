def foxtrot(number):
    return number * 2


def main():
    power_of_two = 1
    for i in range(11):
        print(power_of_two)
        power_of_two = foxtrot(power_of_two)


if __name__ == '__main__':
    main()
