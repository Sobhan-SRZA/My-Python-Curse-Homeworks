# برنامه ای بنویسید که مقادیر a, b, c را از کاربر بگیرد و نتایج عبارات زیر را محاسبه و نمایش دهد:
# عبارت اول:  (a+b*c)<(a*b-c)or(a/b+c)>=(a*b/c)
# عبارت دوم:  not (a>b) and (b==c) or (a+b!=c)
# عبارت سوم:  (a**b>c) and (a//b<c) or not (a%b==c)

import os
os.system("title Barname arzayabi ebarathaye manteghi")

def clear_window():
    os.system("cls")

def print_title(string):
    clear_window()
    title = f"\t{string}"
    print(("-") * (len(title) * 2))
    print(title)
    print(("-") * (len(title) * 2))
    print("\n")

def evaluate_expression(a, b, c):
    try:
        expr1 = (a + b * c) < (a * b - c) or (a / b + c) >= (a * b / c)

    except ZeroDivisionError:
        expr1 = "Khata: Taghsim bar sefr dar ebarat 1"
        
    except Exception as e:
        expr1 = f"Khata: {str(e)}"

    try:
        expr2 = not (a > b) and (b == c) or (a + b != c)

    except Exception as e:
        expr2 = f"Khata: {str(e)}"

    try:
        expr3 = (a ** b > c) and (a // b < c) or not (a % b == c)

    except ZeroDivisionError:
        expr3 = "Khata: Taghsim bar sefr dar ebarat 3"
        
    except Exception as e:
        expr3 = f"Khata: {str(e)}"

    return expr1, expr2, expr3

def print_truth_table():
    print("\nJadval dorosti baraye ebaratha:")
    print("-" * 130)
    print(f"| a | b | c | {"Ebarat 1":<36} | {"Ebarat 2":<36} | {"Ebarat 3":<36} |")
    print("-" * 130)
    
    for a in [0, 1]:
        for b in [0, 1]:
            for c in [0, 1]:
                expr1, expr2, expr3 = evaluate_expression(a, b, c)
                print(f"| {a} | {b} | {c} | {str(expr1):<36} | {str(expr2):<36} | {str(expr3):<36} |")

    print("-" * 130)

def get_number(name):
    while True:
        try:
            return float(input(f"Lotfan meghdar {name} ra vared konid: "))

        except ValueError:
            choice = print("Vorodi namotabar!")

def main():
    while True:
        a = get_number("a")
        b = get_number("b")
        c = get_number("c")
  
        expr1, expr2, expr3 = evaluate_expression(a, b, c)

        print("-" * 20)
        print(f"Meghdarhaye vorodi: a={a}, b={b}, c={c}")
        print(f"Ebarat 1: (a + b * c) < (a * b - c) or (a / b + c) >= (a * b / c)")
        print(f"Ebarat 2: not (a > b) and (b == c) or (a + b != c)")
        print(f"Ebarat 3: (a ** b > c) and (a // b < c) or not (a % b == c)")
        print("-" * 20)
        print(f"Natije ebarat 1: {expr1}")
        print(f"Natije ebarat 2: {expr2}")
        print(f"Natije ebarat 3: {expr3}")
        
        print_truth_table()
        
        choice = input("\nBaraye edame 'c' va baraye khoroj 'q' ra vared konid: ")
        if choice.lower() == 'q':
            break

print_title("Barname arzayabi ebarathaye manteghi")
main()
print("Barname payan yaft.")