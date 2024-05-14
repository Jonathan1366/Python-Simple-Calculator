print("\nCalculate with Python\n")

class Calculator:
    def __init__(self):
        self.add = lambda a, b: a + b
        self.multiply = lambda c, d: c * d
        self.division = lambda e,f: e/f
        self.reduction = lambda g,h: g-h

#jadikan object for method call
calculate = Calculator()

while True:
    print("\n1. Add ")
    print("2. Multiply ")
    print("3. Division")
    print("4. Reduction")
    print("5 Exit")
    choice = int(input("\nChoose the method: "))

    if choice == 1:
        a, b = map(float, input("\nInput 2 numbers for sum method: ").split())
        print(f"\nResult is {calculate.add(a, b)}")
        
    elif choice == 2:
        c, d = map(float, input("\nInput 2 numbers for multiply method: ").split())
        print(f"\nResult is {calculate.multiply(c, d)}")
        
    elif choice == 3:
        e, f = map(float, input("\nInput 2 numbers for division method: ").split())
        print(f"\nResult is {calculate.division(e, f)}")
    
    elif choice==4:
        g,h = map(float, input("\nInput 2 numbers for reduction method: ").split())
        print(f"\nResult is {calculate.reduction(g,h)}")
    
    elif choice==5:
        print("\nThankyou for using my calculator\nHave a nice day\n")
        break
    else:
        print("Invalid input, suggest with 1, 2, 3, 4 or 5")



