def main():
    for num in range(100, 1001):
        for check in range(2, num):
            if num % check == 0:
                break
        else:
            print(num, end=" | ")


if __name__ == '__main__':
    main()
