import os
os.system("title Student Manager")

def clear_window():
    os.system("cls")

def print_title(string):
    clear_window()
    title = f"\t{string}"
    print(("-") * (len(title) * 2))
    print(title)
    print(("-") * (len(title) * 2))
    print("\n")

def list_to_str(str_list):
    return ', '.join(str_list)

students = {}
field_values = ["full_name", "study_status", "score", "register_time"]
study_status_values = ["Faal", "Mashroot", "Ekhraj"]

# Get inputs
def student_number_input():
    clear_window()
    while True:
        try:
            student_number = int(input("Lotfan shomare daneshjooei ra vared konid: "))

            return student_number

        except ValueError:
            clear_window()
            print("Faghat mitavanid az adad sahih estefade konid!")

def score_input():
    clear_window()
    while True:
        try:
            score = float(input("Lotfan moaddel ra vared konid: "))

            return score

        except ValueError:
            clear_window()
            print("Faghat mitavanid az adad ashari estefade konid!")

def study_status_input():
    clear_window()
    while True:
        study_status = input(f"Lotfan vaziyat tahsili ra vared konid (faghat meghdar haye ro be ro ghabol ast: {list_to_str(study_status_values)}): ")

        if study_status not in study_status_values:
            clear_window()
            print(f"Meghdar voroodi namoatabar ast - (voroodi moatabar:  {list_to_str(study_status_values)})")

        else:
            return study_status

def full_name_input():
    clear_window()
    full_name = input("Lotfan naam va naame khanevadegi daneshjoo ra vared konid: ")

    return full_name

def register_time_input():
    clear_window()
    while True:
        register_time = input("Lotfan tarikhe sabt naame daneshjoo ra vared konid (format dorost: YYYY/MM/DD): ")
        parts = register_time.split('/')
        
        if len(register_time) != 10:
            clear_window()
            print("Format tarikhe vared shode dorost nist! Bayad 10 karakter bashe.")
            continue
        
        if len(parts) != 3:
            clear_window()
            print("Format tarikhe vared shode dorost nist! Bayad ba '/' joda shode bashe.")
            continue
        
        year, month, day = parts
        
        if not (year.isdigit() and month.isdigit() and day.isdigit()):
            clear_window()
            print("Sal, mah va rooz bayad adad bashand.")
            continue
        
        if len(year) != 4 or len(month) != 2 or len(day) != 2:
            clear_window()
            print("Sal bayad 4 ragham, mah va rooz bayad 2 ragham bashand.")
            continue
        
        year_num = int(year)
        month_num = int(month)
        day_num = int(day)
        
        if month_num < 1 or month_num > 12:
            clear_window()
            print("Mah bayad bein 01 ta 12 bashe.")
            continue
        
        if day_num < 1 or day_num > 31:
            clear_window()
            print("Rooz bayad bein 01 ta 31 bashe.")
            continue
                
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

def enter_input():
    return input("Baraye edame Enter ra bezanid...")

# Managers
def add_student():
    full_name = full_name_input()
    student_number = student_number_input()
    score = score_input()
    study_status = study_status_input()
    register_time = register_time_input()

    if student_number in students:
        raise ValueError(f"Shomare daneshjooei {student_number} sabt shode ast!")

    students[student_number] = {
        "full_name": full_name,
        "student_number": student_number,
        "score": score,
        "study_status": study_status,
        "register_time": register_time
    }

    print("Daneshjoo ba shomare daneshjooei ", student_number, " ba movafaghiat sabt shod.")

def change_student(student_number: int, field: str):
    if student_number not in students:
        raise ValueError(f"Shomare daneshjooei {student_number} namoatabar ast!")

    if field not in field_values:
        raise ValueError(f"Voroodi namoatabar, faghat voroodi ro be ro moatabar ast: ({list_to_str(field_values)})")

    students[student_number][field] = get_field_input(field)

    print("Daneshjoo ba shomare daneshjooei ", student_number, " ba movafaghiat taghir yaft.")

def delete_student(student_number: int):
    if student_number not in students:
        raise ValueError(f"Shomare daneshjooei {student_number} namoatabar ast!")

    del students[student_number]
    print(f"Daneshjoo ba shomare daneshjooei {student_number} ba movafaghiat hazf shod.")

while True:
    print_title('Welcome to "Student Manager"')
    print(
        "1. Afzodane Daneshjoo\n"
        "2. Hazfe Daneshjoo\n"
        "3. Taghire Etelaat Daneshjoo\n"
        "4. Liste Daneshjoo haye sabt shode\n"
        "5. Namayeshe Etelaate Daneshjoo\n"
        "6. Khorooj\n"
    )

    choice = input("Yek gozine ra entekhab konid: ")

    if choice == "1":
        clear_window()
        try:
            add_student()

        except Exception as e:
            print("Khata:", e)

        enter_input()

    elif choice == "2":
        clear_window()
        try:
            sn = int(input("Shomare daneshjooei ra baraye hazf vared konid: "))
            delete_student(sn)

        except Exception as e:
            print("Khata:", e)

        enter_input()

    elif choice == "3":
        clear_window()
        try:
            sn = int(input("Shomare daneshjooei ra baraye taghir vared konid: "))
            field = input(f"Filed mored nazar ra vared konid ({list_to_str(field_values)}): ")
            change_student(sn, field)

        except Exception as e:
            print("Khata:", e)

        enter_input()

    elif choice == "4":
        clear_window()
        if not students:
            print("Hich daneshjoo'i sabt nashode ast.")

        else:
            header = f"{'Tarikh Sabt':<15} | {'Vaziyat Tahsili':<15} | {'Moaddel':<7} | {'Naam va Naame Khanevadegi':<30} | {'Shomare Daneshjooei':<20} | {'Radif':<5}"
            print("-" * len(header))
            print(header)
            print("-" * len(header))

            for idx, (sn, info) in enumerate(students.items(), start=1):
                print(f"{info['register_time']:<15} | {info['study_status']:<15} | {str(info['score']):<7} | {info['full_name']:<30} | {str(sn):<20} | {str(idx):<5}")

            print("-" * len(header))

        enter_input()

    elif choice == "5":
        clear_window()
        try:
            sn = int(input("Shomare daneshjooei ra baraye namayesh vared konid: "))
            if sn not in students:
                print("Daneshjoo'i ba in shomare sabt nashode ast.")
                
            else:
                info = students[sn]
                print("\nEtelaat Daneshjoo:")
                line_data = f"{info['full_name']}, {info['student_number']}, {info['score']}, {info['study_status']}, {info['register_time']}"                                   
                print("\n")
                print("\n")
                print("-" * len(line_data))
                print(line_data)
                print("-" * len(line_data))
                print("\n")
                print(f"Naam va Naame Khanevadegi: {info['full_name']}")
                print(f"Shomare Daneshjooei: {info['student_number']}")
                print(f"Moaddel: {info['score']}")
                print(f"Vaziyat Tahsili: {info['study_status']}")
                print(f"Tarikh Sabt: {info['register_time']}")
                
        except Exception as e:
            print("Khata:", e)

        enter_input()

    elif choice == "6":
        print("Khorooj az barname. Bedrood!")
        break

    else:
        clear_window()
        print("Gozine namoatabar ast. Lotfan dobare talash konid.")
        enter_input()