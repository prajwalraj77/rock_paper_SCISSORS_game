import random
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
print(logo)
start_no=0
end_no=100
computer_guess=random.randint(start_no,end_no)
print("welcome to guessing no game")
print(f"enter the no from {start_no} to {end_no} :")
choose_level=input("choose the difficulty 'hard' or 'easy  :")

def guess_game():
    if choose_level=='hard':
        count=5
    elif choose_level=='easy':
        count=10
    flag=False
    while not flag  and count>0:
        print(f"u have {count} to guess the no")
        guess_no=int(input("make a guess "))
        count-=1
        if guess_no==computer_guess:
            print("u win")
            flag=True
        elif guess_no<computer_guess:
            print("guess higher")
        elif guess_no>computer_guess:
            print("  guess lower")
    if not flag:
        print("u lost")
        print(f"computer guess is {computer_guess}")    
         
        
guess_game()
