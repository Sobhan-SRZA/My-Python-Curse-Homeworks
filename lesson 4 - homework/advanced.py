# برنامه ای بنویسید که دو عدد و یک عملگر (+و -و *و /) دریافت کند و عملیات مربوطه را انجام دهد.

import os
os.system("title Mashin Hesab")

def clear_window():
    os.system("cls")

def print_title(string):
    clear_window()
    title = f"\t{string}"
    print(("-") * (len(title) * 2))
    print(title)
    print(("-") * (len(title) * 2))
    print("\n")

def get_input():
    while True:
        try:
            num = input("Adad vared konid (Baraie namayesh natige 'q' ra vared konid): ")

            if num == "q":
                return num
                
            return float(num)
        
        except ValueError:
            clear_window()
            print("Khata: Meghdar vared shode baiad adad sahih ya ashar bashad!")

def enter_input():
    return input("Baraye edame Enter ra bezanid...")

while True:
    print_title("Khosh Amadid Be Barname Mashin Hesab")
    print(
        "1. Amale menha (-)\n"
        "2. Amale gam (+)\n"
        "3. Amale zarb (*)\n"
        "4. Amale taqsim (/)\n"
    )

    choice = input("Lotfan az bein gozineha entekhab konid: ")
    if choice == "1":
        clear_window()
        resualt = get_input()

        if resualt == "q":
            print("Khorooj")
            enter_input()
            continue

        numbers = []
        numbers.append(str(resualt))
        while True:
            num = get_input()
            if num == "q":
                break

            else:
                numbers.append(str(num))
                resualt -= num
        
        if len(numbers) < 1:
            print(
                "Faghat yek adad vared shode ast va amale menha emal nemishavad.\n"
                f"Natige: {resualt}"
            )

        else:
            print("-" * 30)
            print(
                " - ".join(numbers) + f" = {resualt}"
            )
            print("-" * 30)
            print(f"Natije: {resualt}")
            enter_input()        

    elif choice == "2":
        clear_window()
        resualt = get_input()

        if resualt == "q":
            print("Khorooj")
            enter_input()
            continue

        numbers = []
        numbers.append(str(resualt))
        while True:
            num = get_input()
            if num == "q":
                break

            else:
                numbers.append(str(num))
                resualt += num
        
        if len(numbers) < 1:
            print(
                "Faghat yek adad vared shode ast va amale menha emal nemishavad.\n"
                f"Natige: {resualt}"
            )

        else:
            print("-" * 30)
            print(
                " + ".join(numbers) + f" = {resualt}"
            )
            print("-" * 30)
            print(f"Natije: {resualt}")
            enter_input()        

    elif choice == "3":
        clear_window()
        resualt = get_input()

        if resualt == "q":
            print("Khorooj")
            enter_input()
            continue

        numbers = []
        numbers.append(str(resualt))
        while True:
            num = get_input()
            if num == "q":
                break

            else:
                numbers.append(str(num))
                resualt *= num
        
        if len(numbers) < 1:
            print(
                "Faghat yek adad vared shode ast va amale menha emal nemishavad.\n"
                f"Natige: {resualt}"
            )

        else:
            print("-" * 30)
            print(
                " * ".join(numbers) + f" = {resualt}"
            )
            print("-" * 30)
            print(f"Natije: {resualt}")
            enter_input()       

         