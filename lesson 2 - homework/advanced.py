# برنامه ای که نام نام خانوادگی، شماره دانشجویی، معدل، وضعیت تحصیلی (فعال، مشروط، اخراج)، تاریخ ثبت نام YYYY/MM/DD و در نهایت به صورات خطی و ستونی چاپ کند.
import os
os.system("title Student Manager")
def clear_window():
    os.system("cls")

def print_title(string):
    clear_window()
    print(("-") * 50)
    print(f"\t{string}")
    print(("-") * 50)
    print("\n")

students = {}
field_values = ["full_name", "study_status", "score", "register_time"]
study_status_values = ["فعال", "مشروط", "اخراج"]

# Get inputs
def student_number_input():
    try:
        student_number = int(input("لطفا شماره دانشجویی را وارد کنید: "))
    except ValueError:
        print("فقط میتوانید از اعداد صحیح استفاده کنید!")

    return student_number
    
def score_input():
    try:
        score = float(input("لطفا معدل را وارد کنید: "))
    except ValueError:
        print("فقط میتوانید از اعداد اعشاری استفاده کنید!")

    return score

def study_status_input():
    study_status = input(f"لطفا وضعیت تحصیلی را وارد کنید (فقط مقدار های رو به رو قابل قبول است: {", ".join(study_status_values)}): ")

    if study_status not in study_status_values:
        raise ValueError(f"مقدار ورودی نامعتبر است - (ورودی معتبر:  {", ".join(study_status_values)})")

    return study_status

def full_name_input():
    full_name = input("لطفا نام نام خانوادگی دانشجو را وارد کنید: ")

    return full_name

def register_time_input():
    register_time = input("لطفا تاریخ ثبت نام دانشجو را وارد کنید (فرمت درست: YYYY/MM/DD): ")

    return register_time

def get_field_input(field: str):
    match field:
        case "full_name":
            return full_name_input()
        
        case "score":
            return score_input()

        case "study_status":
            return study_status_input()
            
        case "register_time":
            return register_time_input()
        
        case _:
            return None

# Managers
def add_student():
    full_name = full_name_input()
    student_number = student_number_input()
    score = score_input()
    study_status = study_status_input()
    register_time = register_time_input()

    if student_number in students:
        raise ValueError(f"شماره دانشجویی {student_number} ثبت شده است!")

    students[student_number] = {
        full_name,
        student_number,
        score,
        study_status,
        register_time
    }

    print("دانشجو با شماره دانشجویی ", student_number, "با موفقیت ثبت شد.")

def change_student(student_number: int, field: str):
    if student_number not in students:
        raise ValueError(f"شماره دانشجویی {student_number} نا معتبر است!")

    if field not in field_values:
        raise ValueError(f"ورودی نامعتبر فقط ورودی رو به رو معتبر است: ({", ".join(field_values)})")

    students[student_number][field] = get_field_input(field)

    print("دانشجو با شماره دانشجویی ", student_number, "با موفقیت ثبت شد.")

students
# print("\n\n")
# print(f"{full_name},\t{student_number},\t{score},\t{study_status},\t{register_time}")
# print("\n\n")
# print("نام نام خانوادگی:\t", full_name)
# print("شماره دانشجویی:\t\t", student_number)
# print("معدل:\t\t\t", score)
# print("وضیعت تحصیلی:\t\t", study_status)
# print("تاریخ ثبت نام:\t\t", register_time)