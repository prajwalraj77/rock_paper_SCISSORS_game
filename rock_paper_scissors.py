import random
user = int(input("Enter your choice (1. ROCK, 2. PAPER, 3. SCISSORS): "))
random_choice=random.randint(1,3)
if user == 1:
    if random_choice == 1:
        print("DRAW")
    elif random_choice == 2:
        print("U LOST")
    else:
        random_choice == 3
        print("U WON")
        flag = True    
elif user == 2:
    if random_choice == 1:
        print("U won")
    elif random_choice == 2:
        print("DRAW")
    else:
        random_choice == 3
        print("U LOST")            
if user == 3:
    if random_choice == 1:
        print("U LOST")
    elif random_choice == 2:
        print("U WON")
    else:
        random_choice == 3
        print("DRAW")
            
    

    


