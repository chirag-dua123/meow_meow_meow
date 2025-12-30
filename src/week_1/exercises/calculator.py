def run_calculator(a, b, c):
        if c == '+':
            return a + b
        elif c == '-':
            return a - b
        elif c == '*':
            return a * b
        elif c == '/':
            if b != 0:
                return a / b
            else:
                raise ZeroDivisionError("Division by zero")
        else:
            raise ValueError("Invalid operator")
        
def main():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    z = input("Enter operator (+, -, *, /): ")
    return run_calculator(x, y, z)

if __name__ == "__main__":
    try:
        result = main()
        print(f"Result: {result}")
        exit(0)
    except ZeroDivisionError:
        print("Error: Division by zero")
        exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)
## This is the change that I am doing in order to check when I merge this branch (just_to_test) to the main branch.s