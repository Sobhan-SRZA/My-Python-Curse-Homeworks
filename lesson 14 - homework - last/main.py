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
    def __init__(self, id: str, message = "Khata: Karbar ba id {id} yaft nashod!"):
        super().__init__(message.replace("{id}", id or "[no id]"))

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

        return True
    
    raise ContactNotFoundError(id, "Karbar ba id {id} yaft nashod!")

# Editing the contact
def edit_contact():
    pass

# Finding the contact
def find_contact(search: str, find_multipile: bool = False) -> (str | list | None):
    contacts = get_contacts()
    ids = []
    for id, value in contacts.items():
        first_name = value["first_name"]
        last_name = value["last_name"]
        phone = value["phone"]
        if (search.find() == id)\
            or (first_name and (first_name.count(search) > 0))\
            or (last_name and (last_name.count(search) > 0))\
            or any(filter(lambda phone: phone.count(search) > 0, phone)):

            if find_multipile:
                ids.append(id)

            else:
                return id
        
        else:
            continue
    
    if len(ids) < 1:
        return None

    else:
        return ids


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
def get_phone_input(phone: list[str] = []):
        i = 0
        while True:
            phone_check = i <= (len(phone) - 1) and phone[i]
            if phone_check:
                print("Shomare zakhire shode dar in qam =", phone[i])

            contact_phone = input(f"Shomare {i + 1} om mokhatab ra vared konid (baraie khorooj \"e\" befrestid va baraie hazf \"r\"): ")
            if len(contact_phone) < 1:
                if phone_check:
                    print("Meqdar taghir nakard.")
                    i += 1
                    continue

                print("Khata: Vorodi khali ast!")
                continue

            if contact_phone.count("e") > 0:
                if len(phone) < 1:
                    print("Khata: Shoma hich shomarei vared nakardid!")
                    continue

                break

            if contact_phone.count("r") > 0:
                if len(phone) < 1 or len(phone) <= i:
                    print("Khata: Shoma hich shomarei vared nakardid!")
                    continue

                last_number = phone[i]
                phone.remove(last_number)
                print(f"Shomare {last_number} ba movaffaqiat pak shod.")


            elif phone_check:
                phone[i] = contact_phone

            else:
                phone.append(contact_phone)

            i += 1

        return phone

# Find contact from user input
def find_contact_from_input(find_multipile: bool = False):
    while True:
        user_search_input = input("Moshakhasate mokhatab ra vared konid ta peyda shavad: ")
        if len(user_search_input) < 1:
            print("Khata: Voroodi khali ast dobare talash konid!")
            continue

        finded_contact = find_contact(user_search_input, find_multipile)
        if finded_contact:
            return finded_contact

        print("Khata: Mokhatab yaft nashod!")
        user_choice = input("Baraie talash dobare enter konid dar gheire in sorat \"e\" ra type konid. ")

        if user_choice.count("e") > 0:
            break

        continue
    
    return None


# Get contact first name from user input
def get_contact_first_name_input():
    while True:
        contact_first_name = input("Name mokhatab ra vared konid (dar gheire in sorat enter konid): ")
        if len(contact_first_name) < 1:
            contact_first_name = None

        if len(contact_first_name) > 15:
            print("Khata: Tedad horofe name vorodi namotabar had aksar 15 harf mojaz ast!")
            continue

        return contact_first_name

# Get contact last name from user input
def get_contact_last_name_input():
    while True:
        contact_last_name = input("Name khanevadegi mokhatab ra vared konid (dar gheire in sorat enter konid): ")
        if len(contact_last_name) < 1:
            contact_last_name = None

        if len(contact_last_name) > 30:
            print("Khata: Tedad horofe name khanevadegi vorodi namotabar had aksar 15 harf mojaz ast!")
            continue

        return contact_last_name

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
        phone = get_phone_input()

        contact_first_name = get_contact_first_name_input()

        contact_last_name = get_contact_last_name_input()

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

        # A menu for editing items
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

            # Edit first name
            if user_choice == "1":
                contact_first_name = get_contact_first_name_input()
                finded_contact["first_name"] = contact_first_name
                write_database(contacts)
                continue

            # Edit last name
            if user_choice == "2":
                contact_last_name = get_contact_last_name_input()
                finded_contact["last_name"] = contact_last_name
                write_database(contacts)
                continue

            # Edit phone numbers
            if user_choice == "3":
                phone = get_phone_input(finded_contact["phone"])
                finded_contact["phone"] = phone
                write_database(contacts)
                continue


            # Exit from the menu
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

    # Remove contact 
    if user_choice == "3":
        clear_window()
        contacts = get_contacts()
        user_search_input = find_contact_from_input()
        try:
            delete_contact(user_search_input)
            print("Mokhatab ba movafaqiat hazf shod.")
        
        except ContactNotFoundError as e:
            print(e)

        enter()
        continue

    # Search for contact 
    if user_choice == "4":
        user_search_input: list[str] = find_contact_from_input(find_multipile=True)
        while True:
            contacts = get_contacts()
            contacts_menu = {}
            index = 0
            step = None
            for id in user_search_input:
                contact = contacts.get(id)
                index += 1
                step = str(index)
                contacts_menu[step] = f"{step}. {str(contact["first_name"]):>10} {str(contact["last_name"]):>20} | Phone: {", ".join(contact["phone"])}"

            contacts_menu[str(index + 1)] = f"{str(index + 1)}. Khorooj"
            print_menu(contacts_menu, "Finded Contacts")
            user_choice = input("Yek gozineh entekhab konid: ")

            # Check menu choices 
            if user_choice not in contacts_menu.keys():
                print(f"Khata: Voroodi na motabar! ({", ".join(contacts_menu.keys())})")
                enter()
                continue

            # Exit from the menu
            if contacts_menu[user_choice].count("Khorooj") > 0:
                break
            
            phone_numbers = contacts_menu[user_choice].split(":")[1].replace(" ", "").split(",") 
            contact_id = find_contact(phone_numbers[0])
            finded_contact = contacts.get(contact_id)
            manager_menu_items = {
                "1": f"1. Virayeshe name (name feli: {finded_contact["first_name"]})",
                "2": f"2. Virayeshe name khanevadegi (name khanevadegi feli: {finded_contact["last_name"]})",
                "3": f"3. Virayeshe shomare telephone (shomare telephone feli: {", ".join(finded_contact["phone"])})",
                "4": "4. Hazfe mokhatab",
                "5": "5. Khorooj"
            }
            print_menu(
                manager_menu_items,
                "\tManager Menu"
            )
            user_choice = input("Yek gozineh entekhab konid: ")

            # Check menu choices 
            if user_choice not in manager_menu_items.keys():
                print(f"Khata: Voroodi na motabar! ({", ".join(manager_menu_items.keys())})")
                enter()
                continue

            # Edit first name
            if user_choice == "1":
                contact_first_name = get_contact_first_name_input()
                finded_contact["first_name"] = contact_first_name
                write_database(contacts)
                continue

            # Edit last name
            if user_choice == "2":
                contact_last_name = get_contact_last_name_input()
                finded_contact["last_name"] = contact_last_name
                write_database(contacts)
                continue

            # Edit phone numbers
            if user_choice == "3":
                phone = get_phone_input(finded_contact["phone"])
                finded_contact["phone"] = phone
                write_database(contacts)
                continue

            # Remove the contact
            if user_choice == "4":
                try:
                    delete_contact(contact_id)
                    print("Mokhatab ba movafaqiat hazf shod.")
                
                except ContactNotFoundError as e:
                    print(e)
                
                break

            # Exit from the menu
            if user_choice == "5":
                break
            

        enter()
        continue


    # Show the all contacts 
    if user_choice == "5":
        contacts = get_contacts()
        if len(contacts.keys()) < 1:
            print("Khata: Hich mokhatabi sabt nashode ast.")

        else:
            print("-" * 110)
            for index, (id, value) in enumerate(contacts.items()):
                print(f"{index + 1}. Name: {str(value["first_name"]):<15} | Name khanevadegi: {str(value["last_name"]):<30}\t | Telephone: {", ".join(value["phone"])}")

            print("-" * 110)

        enter()
        continue

    if user_choice == "6":
        print("Dobare mibinamet khoda negahdar.")
        break