import random

symbols = ['🍇', '🍎', '🍌']

def spin_row():
    row = []
    for i in range(3):
        value = random.choice(symbols)
        value1 = random.choice(symbols)
        value2 = random.choice(symbols)
        return value, value1, value2

def payout(bet, row):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍌':
            print("----------CONGRATULATIIONS----------")
            print("----------YOU WON----------")
            return bet * 3
        elif row[0] == '🍇':
            print("----------CONGRATULATIIONS----------")
            print("----------YOU WON----------")
            return bet * 6
        elif row[0] == '🍎':
            print("----------CONGRATULATIIONS----------")
            print("----------YOU WON----------")
            return bet * 10
    else:
        print("--------------YOU LOST MATCH--------------")
        return 0

balance = 100
print("________WELCOME TO PYTHON  CASTLE________")
print(" ")
print(f"your balance is {balance}")
print("SYMBOLS ARE 🍇🍎🍌")
print("lets start the game ")
while balance > 0:
    print(" ")
    print("______________________________________________")
    bet = input("entre your bet or entre (Y/N) to exit: ")

    if not bet.isdigit():
        print("invalid input try again")
        continue

    bet = int(bet)

    if bet > balance:
        print("insuffiecient funds")
        continue

    if bet <= 0:
        print("bet cannot be negative or zero")
        continue


    balance -= bet
    # print(f"your balance is {balance}")
    row = spin_row()
    print(row)
    payment = payout(bet, row)
    # print(payment)
    balance += payment
    print(f"your new balance is : {balance}")
    if balance == 0:
        print("you out of money start game again ")
        break

