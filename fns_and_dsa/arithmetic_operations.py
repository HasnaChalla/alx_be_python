def perform_operation(num1, num2, operation):
    if operation == 'add':
        print(f"result : ", num1 + num2)
    elif operation == 'subtract':
        print(f"result : ", num1 - num2)
    elif operation == 'multiply':
        print(f"result : ", num1 * num2)
    elif operation == 'divide':
        if num2 == 0:
            print("Error: Division by zero")
        else:
            print(f"result : ", num1 / num2)
    else:
        print("Error: Invalid operation")
