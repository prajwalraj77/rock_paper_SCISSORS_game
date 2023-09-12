#Calculator
logo = """
 _____________________
|  _________________  |
| | Prajwal      0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
from replit import clear

print(logo)
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def new_calculation():
    num1 = int(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    flag=True
    while flag:
    
        operation_symbol = input("Pick an operation: ") 
        num2 = int(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer= calculation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        reset=input("y (to continue) , n  (to stop) for fresh calculaton f (start to from new ) :").lower
        if reset=='y':
        
            num1=answer
        if reset=='f':
            clear()
            new_calculation()
            flag=False
            
        elif reset=='n':
            flag=False
new_calculation()




