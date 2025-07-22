def add(x, y):

    return x + y

def subtract(x, y):

    return x - y

def multiply(x, y):

    return x * y

def divide(x, y):

    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def get_number(prompt):

    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_operation():

    operations = {
        '1': ('Addition', add),
        '2': ('Subtraction', subtract),
        '3': ('Multiplication', multiply),
        '4': ('Division', divide)
    }
    
    while True:
        print("\nSelect operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        
        choice = input("Enter choice (1/2/3/4): ")
        
        if choice in operations:
            return operations[choice]
        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")

def main():
    print("=" * 40)
    print("        SIMPLE CALCULATOR")
    print("=" * 40)
    
    while True:

        operation_name, operation_func = get_operation()

        num1 = get_number(f"\nEnter first number: ")
        num2 = get_number(f"Enter second number: ")

        result = operation_func(num1, num2)

        print(f"\n{num1} {operation_name.lower()} {num2} = {result}")
        
        while True:
            continue_calc = input("\nDo you want to perform another calculation? (yes/no): ").lower()
            if continue_calc in ['yes', 'y']:
                break
            elif continue_calc in ['no', 'n']:
                print("Thank you for using the calculator!")
                return
            else:
                print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
