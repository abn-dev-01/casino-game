# Python SLot machine 
import random
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def spin_row():
    """ Purpose: one """
    symbols = ['🔔','🍋','🍉','🍒','⭐']
    # results=[]
    # for i in range(3):
    #     results.append(random.choice(symbols))
    results = [random.choice(symbols) for _ in range(3)]
    return results
# end def


def print_row(row):
    """     Purpose:   print a row of symbols """
    print("*" * 25)
    print(" | ".join(row))
    print("*" * 25)
# end def


def get_payout(row, bet):
    """     Purpose:      """
    if row[0] == row[1] == row[2]:
        # '🔔','🍋','🍉','🍒','⭐']
        if row[0] == '🔔':
            print("JACKPOT!!!")
            return bet * 3
        elif row[0] == '🍋':
            print("JACKPOT!!!")
            return bet * 4
        elif row[0] == '🍉':
            print("JACKPOT!!!")
            return bet * 5
        elif row[0] == '🍒':
            print("JACKPOT!!!")
            return bet * 10
        elif row[0] == '⭐':
            print("JACKPOT!!!")
            return bet * 20
        # end if-2
    # end if-1
    return 0 # nothing matched    
# end def

def main():
    """
    Purpose: 
    """
    balance = 100
    print("*************************************************")
    print("Welcome to the Python Slot Machine!")
    print("Symbols: 🔔,🍋,🍉,🍒,⭐")
    print("You have $100.00")
    print("Each spin costs $1.00")
    print("Match two or more numbers to win!")
    print("Match three numbers to win the JACKPOT!")
    print("Good luck!")
    print("*************************************************")
    print("Press ENTER to spin...")
    
    while balance>0:
        print(f"Balance: ${balance}")
        bet = input("Enter your bet: ")
        if not bet.isdigit():
            print("Invalid bet. Try again.")
            continue
        bet = int(bet)
        if bet > balance:
            print("Insufficient funds. Try again.")
            continue
        if bet <=0:
            print("Invalid bet. Try again. Must be greater than 0")
            continue
        balance -= bet
        
        row = spin_row()
        print("Spinning ...\n")
        print_row(row)
        
        payout = get_payout(row, bet)
        # print(f"Payout: ${payout}")
        
        if payout > 0:
            print(f"Congratulations! You won ${payout}")
        else:
            print("Sorry, you didn't win anything. Try again.")
            
        print("Press ENTER to spin again or type 'exit' to quit...")
        balance += payout

        choice = input()
        if choice.lower() == 'exit':
            break
    
    # end while
    
    
    print("You are out of money. Thanks for playing!")
    print("Goodbye!")
    print("*************************************************")
    print("Game Over")
    print("*************************************************")
    print("Press ENTER to exit...")


# end def

if __name__ == "__main__":
    main()
# end if

# end main.py