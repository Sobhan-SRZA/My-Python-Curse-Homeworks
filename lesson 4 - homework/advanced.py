# برنامه ای بنویسید که دو عدد و یک عملگر (+و -و *و /) دریافت کند و عملیات مربوطه را انجام دهد.

import os
import re

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def display_title(title_text):
    clear_console()
    title = f"\t{title_text}"
    print("-" * (len(title) * 2))
    print(title)
    print("-" * (len(title) * 2))
    print("\n")

def get_valid_number(prompt="Please enter a number: "):
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("Error: Input cannot be empty.")
                continue
            return float(user_input)
        except ValueError:
            print("Error: Please enter a valid number.")

def get_valid_command():
    valid_commands = {"0", "1", "2", "3", "4"}
    while True:
        command = input("Please enter command number (0-4): ").strip()
        if command in valid_commands:
            return command

        print("Error: Please enter a valid command (0-4).")

def get_continue_choice():
    while True:
        choice = input("Do you want to continue? (y/n): ").strip().lower()
        if choice in {"y", "n"}:
            return choice == "y"
        print("Error: Please enter 'y' or 'n'.")

def validate_expression(expr):
    # Basic validation for safe arithmetic expression
    # Allow numbers, operators (+-*/), and parentheses
    safe_pattern = r'^[\d\s\+\-\*/\(\)\.]+$'
    if not re.match(safe_pattern, expr):
        return False
        
    try:
        # Test evaluation with restricted globals/locals
        eval(expr, {"__builtins__": None}, {})
        return True

    except:
        return False

def get_valid_expression():
    while True:
        expr = input("Please enter your calculation string: ").strip()
        if not expr:
            print("Error: Input cannot be empty.")
            continue
        
        if validate_expression(expr):
            return expr
        
        print("Error: Invalid expression. Use numbers and operators (+, -, *, /) only.")


# Start program
os.system("title Console Calculator")

while True:
    display_title("Welcome to Console Calculator")
    print(
        "0. Evaluate Expression",
        "1. Addition",
        "2. Subtraction",
        "3. Multiplication",
        "4. Division",
        sep="\n"
    )
    print("\n")
    
    command = get_valid_command()

    if command == "0":
        display_title("Evaluate Expression")
        expr = get_valid_expression()
        try:
            result = eval(expr, {"__builtins__": None}, {})
            print(f"Result: {result}")
    
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
    
        except Exception as e:
            print(f"Error: Invalid calculation ({str(e)}).")
    
        input("\nPress Enter to continue...")

    elif command == "1":
        display_title("Addition")
        result = 0
        while True:
            num = get_valid_number()
            result += num
            if not get_continue_choice():
                break
    
        print(f"Sum: {result}")
        input("\nPress Enter to continue...")

    elif command == "2":
        display_title("Subtraction")
        result = None
        while True:
            num = get_valid_number()
            result = num if result is None else result - num
            if not get_continue_choice():
                break
    
        if result is not None:
            print(f"Result: {result}")
    
        input("\nPress Enter to continue...")

    elif command == "3":
        display_title("Multiplication")
        result = 1
        while True:
            num = get_valid_number()
            result *= num
            if not get_continue_choice():
                break
    
        print(f"Product: {result}")
        input("\nPress Enter to continue...")

    elif command == "4":
        display_title("Division")
        result = None
        while True:
            num = get_valid_number()
            if num == 0 and result is not None:
                print("Error: Division by zero is not allowed.")
                continue
            result = num if result is None else result / num
            if not get_continue_choice():
                break
    
        if result is not None:
            print(f"Result: {result}")
    
        input("\nPress Enter to continue...")