# برنامهای بنو یسید که عددی را از کاربر1 بگیرد و کاربر2 عددی را حدس بزند. در صورتیکه عدد وارد شده برابر با مقدارعدد وارد شده توسط کاربر 1 نباشد اعداد را مقایسه و اگر از مقدار وارد شده کاربر1 کوچکتر باشد در خروجی کوچکتر است و در صورتی که بزرگ باشد بزرگتر است نشان داده شود؟تا جایی که عدد را درست حدس بزند. 

import os

def clear_console():
    os.system("cls")


def get_number_input(first=False):
    while True:
        try:
            if first:
                number = int(input("Bazikone 1 lotfan adade X ra vared konid: "))

                return number
            
            else:
                number = int(input("Bazikone 2 Hadse khod ra vared konid: "))

                return number

        except ValueError:
            clear_console()
            print("Khata: Faghat adade sahih vared konid!")

def press_enter():
    input("Baraie edame enter bezanid ...")

clear_console()
print("Bazi Hadse Adad - Bazikone 1")
tries = 0
x_number = get_number_input(True)
while True:
    clear_console()
    print("Bazi Hadse Adad - Bazikone 2")
    guess = get_number_input()
    tries += 1

    if guess < x_number:
        print(f"Natije hads: {guess} < X")
        press_enter()

    elif guess > x_number:
        print(f"Natije hads: {guess} > X")
        press_enter()
    
    else:
        print(f"Afarin shoma ba {tries} hads tonestid X ra peyda konid. | {guess} = X")
        press_enter()
        break

print("Etmame bazi. Kheili khosh gozasht.")