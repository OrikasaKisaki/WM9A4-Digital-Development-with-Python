def add(n1,n2):
    return n1 + n2

def substract(n1,n2):
    return n1 - n2

def multiple(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiple")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4):")

    n1 = float(input("Enter first number:"))
    n2 = float(input("Enter second number:"))

    if choice == "1":
        print("Result:", add(n1,n2))
    elif choice == "2":
        print("Result:", substract(n1,n2))
    elif choice == "3":
        print("Result:", multiple(n1,n2))
    elif choice == "4":
        print("Result:", divide(n1,n2))
    else:
        print("Invalid input.")

calculator()
