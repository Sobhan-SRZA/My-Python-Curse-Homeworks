# برنامه ای بنویسید که نام و نمره سه درس ریاضی، فیزیک و شیمی مربوط به چندین دانشج و را از
# ورودی دریافت و در دیکشنری تو در تویی ذخیره کرده و اعمال زیر را روی آنها انجام دهد:
# .۱ میانگین نمرات هر دانشجو را محاسبه و به دی کشنری اضافه کنید
# .۲ دانشجویی که باالتر ی ن میانگین را دارد پیدا کن ید
# .۳ لیست دانشجو یانی که در درس "physics "نمره باالی ۱۷ گرفته اند را نمایش دهید 

students = {}

while True:
    print("\n=== MENU ===")
    print("1. Ezafe kardan daneshjoo")
    print("2. Mohasebe va namayesh miyangin har daneshjoo")
    print("3. Peyda kardan daneshjoo ba bala-tarin miyangin")
    print("4. Namayesh daneshjooyi ke dar physics nomre bala-tar az 17 daran")
    print("5. Namayesh hameye daneshjoo ha")
    print("6. Virayesh daneshjoo")
    print("7. Hazf daneshjoo")
    print("8. Khorooj")
    
    choice = input("Entekhab konid (1-8): ")

    if choice == "1":
        name = input("Name daneshjoo: ")


        math = None
        while True:
            math = input("Nomre riazi: ")
            if not math.replace('.', '', 1).isdigit():
                print("Nomre na motabar!")
                continue
            
            math = float(math)
            break

        physics = None
        while True:
            physics = input("Nomre fizik: ")
            if not physics.replace('.', '', 1).isdigit():
                print("Nomre na motabar!")
                continue

            physics = float(physics)
            break

        chemistry = None
        while True:
            chemistry = input("Nomre shimi: ")
            if not chemistry.replace('.', '', 1).isdigit():
                print("Nomre na motabar!")
                continue
            
            chemistry = float(chemistry)
            break

        students[name] = {
            "riazi": math,
            "physics": physics,
            "shimi": chemistry
        }

        print("Daneshjoo ba movafaghiat ezafe shod.")
        input("\nBaraie edameh enter konid...")

    elif choice == "2":
        if not students:
            print("Hich daneshjooei sabt nashode.")
            input("\nBaraie edameh enter konid...")
            continue

        print("\nMiyangin har daneshjoo:")
        for name in students:
            r = students[name]["riazi"]
            p = students[name]["physics"]
            s = students[name]["shimi"]
            avg = (r + p + s) / 3
            students[name]["miyangin"] = avg
            print(name + ": " + str(round(avg, 2)))

        input("\nBaraie edameh enter konid...")

    elif choice == "3":
        if not students:
            print("Hich daneshjooei sabt nashode.")
            input("\nBaraie edameh enter konid...")
            continue

        best_name = ""
        best_avg = 0
        for name in students:
            if "miyangin" in students[name]:
                avg = students[name]["miyangin"]
            else:
                avg = (students[name]["riazi"] + students[name]["physics"] + students[name]["shimi"]) / 3
                students[name]["miyangin"] = avg

            if avg > best_avg:
                best_avg = avg
                best_name = name

        print("Behtarin daneshjoo: " + best_name + " ba miyangin " + str(round(best_avg, 2)))
        input("\nBaraie edameh enter konid...")

    elif choice == "4":
        if not students:
            print("Hich daneshjooei sabt nashode.")
            input("\nBaraie edameh enter konid...")
            continue

        print("Daneshjooyani ke dar physics nomre > 17 daran:")
        has_found = False
        for name in students:
            if students[name]["physics"] > 17:
                print("- " + name)
                has_found = True
        if not has_found:
            print("Hich daneshjooei peyda nashod.")

        input("\nBaraie edameh enter konid...")

    elif choice == "5":
        if not students:
            print("Hich daneshjooei sabt nashode.")
            input("\nBaraie edameh enter konid...")
            continue

        print("\nList-e daneshjoo ha:")
        for name in students:
            d = students[name]
            print(f"- {name}: Riazi={d['riazi']}, Physics={d['physics']}, Shimi={d['shimi']}", end='')
            if "miyangin" in d:
                print(f", Miyangin={round(d['miyangin'], 2)}")
            else:
                print()

        input("\nBaraie edameh enter konid...")

    elif choice == "6":
        name = input("Name daneshjoo baraye virayesh: ")
        if name not in students:
            print("In daneshjoo vojood nadarad.")
            input("\nBaraie edameh enter konid...")
            continue

        new_math = None
        while True:
            new_math = input(f"Nomre jadid riazi (ghabli: {students[name]['riazi']}): ")
            if not new_math.replace('.', '', 1).isdigit():
                print("Nomre na motabar!")
                continue
            
            students[name]["riazi"] = float(new_math)
            break

        new_physics = None
        while True:
            new_physics = input(f"Nomre jadid physics (ghabli: {students[name]['physics']}): ")
            if not new_physics.replace('.', '', 1).isdigit():
                print("Nomre na motabar!")
                continue
            
            students[name]["physics"] = float(new_physics)
            break


        new_chem = None
        while True:
            new_chem = input(f"Nomre jadid shimi (ghabli: {students[name]['shimi']}): ")
            if not new_chem.replace('.', '', 1).isdigit():
                print("Nomre na motabar!")
                continue
            
            students[name]["shimi"] = float(new_chem)
            break

        if "miyangin" in students[name]:
            del students[name]["miyangin"]

        print("Etela'at daneshjoo virayesh shod.")
        input("\nBaraie edameh enter konid...")

    elif choice == "7":
        name = input("Name daneshjoo baraye hazf: ")
        if name in students:
            del students[name]
            print("Daneshjoo hazf shod.")
        else:
            print("In daneshjoo vojood nadarad.")
            
        input("\nBaraie edameh enter konid...")

    elif choice == "8":
        print("Barname ba movafaghiat khateme yaft.")
        break

    else:
        print("Entekhab na motabar! Yek adad az 1 ta 8 vared konid.")
        input("\nBaraie edameh enter konid...")