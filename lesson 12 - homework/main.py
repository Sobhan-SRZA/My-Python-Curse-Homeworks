# برنامهای بنو یسید که:
# o یک فایل متنی با نام txt.notes ایجاد کند
# o از کاربر ۳ یادداشت دریافت کند و در فایل ذخیره نماید
# o محتوای فایل را نمای ش دهد

main_file_path = __file__.replace("main.py", "")
file_path = main_file_path + "note.txt"

def write_notes(content):
    with open(file_path, "a") as file:
        file.write(content + "\n")
    
    return file_path

def read_notes():
    with open(file_path, "r") as file:
        return file.read()

print("\n")
print("Be Barnameie \"Sabte Yaddasht\" Khosh Amadid")
print("\n" * 2)
while True:
    print("dar sorate khoroog \"exit\" type konid!")
    print("Yaddasht haie khodra vared konid.")
    user_input = input(">> ")
    if user_input == "exit":
        break
    
    else:
        write_notes(user_input)

user_input = input("Baraie print mohtavaie file note.txt kelide \"y\" ra vared konid: ")

if user_input == "y":
    print(read_notes())

else:
    print("Barname be payan resid.")