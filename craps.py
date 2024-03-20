import random as rd

def dice():
    return rd.randint(1,6), rd.randint(1,6)

def game():
    first = sum(dice())
    print(f"Sum is {first}")
    
    if first == 7 or first == 11:
        print("You won!")
        return
    elif first == 2 or first == 3 or first == 12:
        print("Craps! You lose!")
        return
    else:
        a = first
        print(f"Your goal is: {a}")
        
        while True:
            b = sum(dice())
            print(f"Next is {b}")
            
            if b == 7:
                print("You lose!")
                return
            elif b == a:
                print("You win!")
                return
game()