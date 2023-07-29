MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposite():
    while True:
        amount = input("What you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
             return amount
            else:
             print("amount must be greater than 0")
        else:
         print("Enter a number please")


def get_Number_of_lines():
       while True:
        line = input("Enter the nubmer of lines that you bet on (1-" + str(MAX_LINES) + ")? ")
        if line.isdigit():
            line = int(line)
            if 1 <= line<= MAX_LINES :
             return line
            else:
             print("Enter a valid number of lines.")
        else:
         print("Enter a number please")


def get_Bet():
       while True:
        amount = input("How much money you want to bet on each line? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount<= MAX_BET :
             return amount
            else:
             print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
         print("Enter a number please")
  

def main():
    balance = deposite();
    lines = get_Number_of_lines();
    bet = get_Bet();
    print(balance, lines)
main()
