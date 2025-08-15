# برنامه ی مدیریت مخاطبین
import os
import json

# Database files path
main_file_path = __file__.replace("main.py", "")
file_name = "contacts.json"

# Database template
"""
[id]:{
    "first_name": "",
    "last_name": "",
    "phone": [""],
}
"""

# Custom error for not found the contatc
class ContactNotFoundError(Exception):
    def __init__(self, id: str, message = "Karbar ba id {id} yaft nashod!"):
        super().__init__(message.format(id))

    pass

# Clear the console
def clear_window():
    os.system("cls")

# Write the all data to the database json file
def write_database(input_object: object):
    with open(main_file_path + file_name, "w") as file:
        file.write(json.dumps(input_object, sort_keys=True))
        return True

# Read database json file
def read_database():
    try:
        with open(main_file_path + file_name, "r") as file:
            return json.loads(file.read())
    
    except:
        return None

# Get all contacts from database
def get_contacts():
    return read_database() or {}

# Getting last id of contact from database
def get_last_contact_id():
    contacts = get_contacts()
    if len(contacts) < 1:
        return 0
        
    return int(next(reversed(contacts)))

# Add contact to the database
def add_contact(phone: list[str], first_name: str = None, last_name: str = None):
    contacts = get_contacts()
    last_id = get_last_contact_id()
    new_contact_id = str(last_id + 1)
    if not (type(phone) == list):
        phone = [phone]
    
    contacts[new_contact_id] = {
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone
    }

    new_contact = contacts[new_contact_id]

    write_database(contacts)

    return new_contact

# Delete the contact
def delete_contact(id: str):
    contacts = get_contacts()
    finded_contact = contacts.get(id)

    if finded_contact:
        contacts.__delitem__(id)
        write_database(contacts)

    
    raise ContactNotFoundError(id, "Karbar ba id {id} yaft nashod!")

# Editing the contact
def edit_contact():
    pass

# Finding the contact
def find_contact(search: str):
    contacts = get_contacts()
    for id, value in contacts.items():
        first_name = value["first_name"]
        last_name = value["last_name"]
        phone = value["phone"]
        if (id == search)\
            or (first_name and (first_name.count(search) > 0))\
            or (last_name and (last_name.count(search) > 0))\
            or filter(lambda phone: phone.count(search) > 0, phone):

            return (id, value)
        
        else:
            continue
    
    return None


# Get integer from the user by custom input description and filtering zero input.
def get_int(input_describe: str = "Adad ra vared konid: ", skip_zero: bool = False):
    while True:
        try:
            user_input = int(input(input_describe))
            if skip_zero and (user_input < 1):
                print("Khata: Adade zire 1 morede qabol nist!")
                continue

            return user_input
        
        except ValueError:
            print("Khata: Vorodi namotabar! (Faqat adad motabar ast)")
            continue


# Return phone numbers from user enter
def getPhoneInput() -> list[str]:
        phone = []
        i = 0
        while True:
            contact_phone = input(f"Shomare {i + 1} om mokhatab ra vared konid (baraie khorooj \"e\" befrestid): ")
            if len(contact_phone) < 1:
                print("Khata: Vorodi khali ast!")
                continue

            if "e" in contact_phone:
                if len(phone) < 1:
                    print("Khata: Shoma hich shomarei vared nakardid!")
                    continue

                break

            phone.append(contact_phone)
            i += 1

        return phone

# Find contact from user input
def find_contact_from_input():
    while True:
        user_search_input = input("Moshakhasate mokhatab ra vared konid ta peyda shavad: ")
        if len(user_search_input) < 1:
            print("Khata: Voroodi khali ast dobare talash konid!")
            continue

        finded_contact, __ = find_contact(user_search_input)
        if finded_contact:
            return finded_contact

        print("Khata: Mokhatab yaft nashod!")
        user_choice = input("Baraie talash dobare enter konid dar gheire in sorat \"e\" ra type konid. ")

        if "e" in user_choice:
            break

        continue
    
    return None


menu_items = {
    "1": "1. Afzoodane mokhatab",
    "2": "2. Viraieshe mokhatab",
    "3": "3. Hazfe mokhatab",
    "4": "4. Jostojoe mokhatab",
    "5": "5. Namayeshe mokhatab ha",
    "6": "6. Khoorooj az barnameh"
}

# Printing the menu in console
def print_menu(menu: dict[str, str] = menu_items, menu_title = "\tMenu"):
    print( "=" * 20 )
    print(menu_title)
    print( "=" * 20 )
    for item in menu.values():
        print(item)

# For printing welcome message in console
def print_welcome():
    clear_window()
    print( "=" * 45 )
    print("Be Barnameh Modiriat Mokhateben Khosh Amadid")
    print( "=" * 45 )
    print( "\n")

# An input for make a stop before next step
def enter():
    input("Baraie edame enter konid.")

# Main app
clear_window()
while True:
    print_welcome()
    print_menu()
    user_choice = input("Yek gozineh entekhab konid: ")

    # Check menu choices 
    if user_choice not in menu_items.keys():
        print(f"Khata: Voroodi na motabar! ({", ".join(menu_items.keys())})")
        enter()
        continue

    # Add contact
    if user_choice == "1":
        clear_window()
        phone = getPhoneInput()

        contact_first_name = input("Name mokhatab ra vared konid (dar gheire in sorat enter konid): ")
        if len(contact_first_name) < 1:
            contact_first_name = None

        contact_last_name = input("Name khanevadegie mokhatab ra vared konid (dar gheire in sorat enter konid): ")
        if len(contact_last_name) < 1:
            contact_last_name = None

        add_contact(phone=phone, first_name=contact_first_name, last_name=contact_last_name)

        print("Mokhatab ba movafaqiat ezafe shod.")
        enter()
        continue
    
    # Edit contact
    if user_choice == "2":
        clear_window()
        contacts = get_contacts()
        user_search_input = find_contact_from_input()
        finded_contact = contacts.get(user_search_input)
        while True:
            edit_menu_items = {
                "1": f"1. Virayeshe name (name feli: {finded_contact["first_name"]})",
                "2": f"2. Virayeshe name khanevadegi (name khanevadegi feli: {finded_contact["last_name"]})",
                "3": f"3. Virayeshe shomare telephone (shomare telephone feli: {", ".join(finded_contact["phone"])})",
                "4": "4. Khorooj"
            }
            print_menu(
                edit_menu_items,
                "\tEdit Menu"
            )
            user_choice = input("Yek gozineh entekhab konid: ")

            # Check menu choices 
            if user_choice not in edit_menu_items.keys():
                print(f"Khata: Voroodi na motabar! ({", ".join(edit_menu_items.keys())})")
                enter()
                continue

            if user_choice == "1":
                contact_first_name = input("Name mokhatab ra vared konid: ")
                if len(contact_first_name) < 1:
                    contact_first_name = None
          
                finded_contact["first_name"] = contact_first_name
                write_database(contacts)
                continue


            if user_choice == "2":
                contact_last_name = input("Name khanevadegie mokhatab ra vared konid: ")
                if len(contact_last_name) < 1:
                    contact_last_name = None

                finded_contact["last_name"] = contact_last_name
                write_database(contacts)
                continue

            if user_choice == "3":
                finded_contact["phone"] = contact_phone
                write_database(contacts)
                continue


            if user_choice == "4":
                break

        print("Mokhatab ba movafaqiat virayesh shod.")
        print("=" * 20)
        print("Name:", finded_contact["first_name"])
        print("Name khanevadegi:", finded_contact["last_name"])
        print("Shomare telephone ha:", ", ".join(finded_contact["phone"]))
        print("=" * 20)
        enter()
        continue

    if user_choice == "3":
        clear_window()
        phone = []
        phone_num_count = get_int("In mokhatab chand shomare darad? ", True)
        for i in range(phone_num_count):
            contact_phone = input(f"Shomare {i + 1} om mokhatab ra vared konid: ")
            phone.append(contact_phone)

        contact_first_name = input("Name mokhatab ra vared konid (dar gheire in sorat enter konid): ")
        if len(contact_first_name) < 1:
            contact_first_name = None

        contact_last_name = input("Name khanevadegie mokhatab ra vared konid (dar gheire in sorat enter konid): ")
        if len(contact_last_name) < 1:
            contact_last_name = None

        add_contact(phone=phone, first_name=contact_first_name, last_name=contact_last_name)

        print("Mokhatab ba movafaqiat ezafe shod.")
        enter()
        continue

    if user_choice == "6":
        print("Dobare mibinamet khoda negahdar.")
        break