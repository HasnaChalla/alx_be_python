def perform_operation(num1, num2, operations):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input(
        "Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    operations = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y if y != 0 else "Error: Division by zero is not allowed."
    }
    if operation in operations:
        print(f"Result: ", operations[operation](num1, num2))
    else:
        print("Error: Invalid operation.")


perform_operation(5, 6, 'add')
