import math

def calculator():
    print("------ Scientific Calculator ------")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Square Root")
    print("7. Factorial")
    print("8. sin(x), cos(x), tan(x)")
    print("9. Logarithm (log10)")
    print("0. Exit")

    while True:
        choice = input("\nEnter your choice (0 to exit): ")

        if choice == '1':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", a + b)

        elif choice == '2':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", a - b)

        elif choice == '3':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", a * b)

        elif choice == '4':
            a = float(input("Enter numerator: "))
            b = float(input("Enter denominator: "))
            if b != 0:
                print("Result:", a / b)
            else:
                print("Error: Division by zero")

        elif choice == '5':
            a = float(input("Enter base: "))
            b = float(input("Enter exponent: "))
            print("Result:", math.pow(a, b))

        elif choice == '6':
            a = float(input("Enter number: "))
            print("Result:", math.sqrt(a))

        elif choice == '7':
            a = int(input("Enter a number (non-negative integer): "))
            if a >= 0:
                print("Result:", math.factorial(a))
            else:
                print("Error: Factorial not defined for negative numbers")

        elif choice == '8':
            x = float(input("Enter angle in degrees: "))
            rad = math.radians(x)
            print("sin(x):", math.sin(rad))
            print("cos(x):", math.cos(rad))
            print("tan(x):", math.tan(rad))

        elif choice == '9':
            x = float(input("Enter number (>0): "))
            if x > 0:
                print("log10(x):", math.log10(x))
            else:
                print("Error: log undefined for 0 or negative numbers")

        elif choice == '0':
            print("Exiting Calculator. Goodbye!")
            break

        else:
            print("Invalid choice! Please select from the menu.")

# Run the calculator
calculator()
