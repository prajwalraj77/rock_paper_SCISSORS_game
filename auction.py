logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
import replit 
bidders={}
while True:
    
    name=input("Enter the name ")
    bid=int(input("Enter the bid amount "))
    bidders[name]=bid
    again=input(" enter yes to bid or no to cancel ")
    if again =="no":
        break
    replit.clear()
print(bidders)
bid_winner=0
bid_winner_name=""
for i in bidders:
    new_bid=bidders[i]
        
    if bid_winner<new_bid:
        bid_winner=new_bid
        bid_winner_name=i
print(f" bid winner is {bid_winner_name} and the amount is  {bid_winner}")


 