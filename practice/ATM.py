import sys

money = 1000


def main():
    break_loop = False
    while not break_loop:

        choice = menu()

        if choice == 1:
            user_bal()

        elif choice == 2:
            deposit()

        elif choice == 3:
            withdraw()

        elif choice == 4:
            break_loop = True
            sys.exit()


def user_bal():
    global money
    print(f"current balance: {money}")


def menu():
    try:
        choice = int(
            input(
                "select one of the following: \n1. Check balance \n2. Deposit money \n3. Withdraw money \n4. Exit program \nchoice: "
            )
        )
        if choice - 1 not in list(range(4)):
            raise ArithmeticError
    except ValueError:
        print("please enter a valid integer\n")
    except ArithmeticError:
        print("please enter a valid integer\n")

    try:
        return choice
    except UnboundLocalError:
        pass


def deposit():
    global money
    try:
        amount = int(input("enter the amount of money to deposit: "))
        if amount < 0:
            raise ValueError
        money = money + amount
        print("deposit complete!\n")
        user_bal()

    except ValueError:
        print("\nenter an appropriate number\n")


def withdraw():
    global money
    try:
        amount = int(input("enter the amount of money to withdraw: "))
        if amount > money:
            print("\ninsufficient funds\n")
        if amount < 0:
            raise ArithmeticError
        else:
            money = money - amount
            print("\nwithdrawal complete!\n")
            user_bal()
    except ValueError:
        print("\nenter an appropriate number\n")
    except ArithmeticError:
        print("\nenter an appropriate number\n")


main()
