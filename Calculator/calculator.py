# Calculator (CLI) – Simple console app using Python basics

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def main():
    while True:
        print("\n=== CALCULATOR MENU ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "5":
            print("Goodbye! 👋")
            break
        
        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please choose 1–5.")
            continue
        
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue
        
        if choice == "1":
            print(f"Result: {add(a, b)}")
        elif choice == "2":
            print(f"Result: {subtract(a, b)}")
        elif choice == "3":
            print(f"Result: {multiply(a, b)}")
        elif choice == "4":
            print(f"Result: {divide(a, b)}")

if __name__ == "__main__":
    main()
