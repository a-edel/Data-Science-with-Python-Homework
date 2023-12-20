def main():
    color = input("What is your favorite color? 1. Blue 2. Red 3. Green ")
    match color:
        case "1":
            print("Good choice.")
        case "2":
            print("Poor choice.")
        case "3":
            print("Not a bad choice.")
        case _:
            print("Not a primary color.")


if __name__ == '__main__':
    main()
