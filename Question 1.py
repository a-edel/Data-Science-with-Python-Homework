def main():
    interest_rate = float(input("What is the interest rate? "))
    principal = float(input("What is the principal? "))
    years = float(input("What is the number of years? "))
    amount = principal * (1 + interest_rate / 100) ** years
    print(f"Amount earned: {amount:,.2f}")


if __name__ == '__main__':
    main()
