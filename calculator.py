def basic_arithmetic():
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))
    operation = input("Choose operation (+ , - , * , / ) : ")
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error ! Divided bye 0")
           
    return result

def advanced_arithmetic():
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))
    operation = input("Choose operation (% , ** , // ) : ")
    if operation == '%':
        result = num1 % num2
    elif operation == '**':
        result = num1 ** num2
    elif operation == '//':
        if num2 != 0:
            result = num1 // num2
        else:
            print("Error ! Division by 0")
    return result

def complex_arithmetic():
    num1 = complex(input("Enter 1st number: "))
    num2 = complex(input("Enter 2nd number: "))
    operation = input("Choose operation (+ , - , * , / ) : ")
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error ! Divided bye 0")
           
    return result

def operation():
    while True:
        print("Welcome...")
        print("Choose 1 for basic arithmetic(), 2 for advanced arithmetic() and 3 for complex ")
        choose = int(input("Enter choice: "))
        if choose == 1:
            print(basic_arithmetic())
        elif choose == 2:
            print(advanced_arithmetic())
        elif choose == 3:
            print(complex_arithmetic())
        else:
            print("Invalid Choice")

        repeat = input("Do you want to repeat calculator if yes then type yes ").lower()
        if repeat != 'yes':
            print("Bye Bye")
            break
operation()