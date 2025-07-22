# 2 لیست با تعداد برابری از دانشجویان و نمره آن دانشجویان در یک لیست را از ورودی
# دریافت کنید.
# ▪ با استفاده از zip ای ن دو لی ست را ترکیب کنید.
# ▪ برای هر دانشجو نام و نمره اش را چاپ کنید.
# ▪ نام دانشجویانی که نمره باالتر از 16 دارند را در لیست جدید ذخ یره کنید.

stiudents = []
scores = []

while True:
    print(
        "1. Afzoodane daneshjoo\n"+
        "2. Hazfe daneshjoo\n"+
        "3. Viraiesh daneshjoo\n"+
        "4. Namaieshe daneshjoo ha\n"+
        "5. Khorooj"
    )

    print("\n")
    choice = input("Az gozine ha entekhab konid: ")

    if choice == "1":
        print("Afzoodane Daneshjoo")
        print("\n")
        
        name = input("Naame daneshjoo ra vared konid: ")
        score = float(input("Nomre daneshjoo ra vared konid: "))

        stiudents.append(name)
        scores.append(score)

        print(f"Daneshjoo ba moshakhasate ro be ro afzode shod: {name} - {score}")
        input("Baraie edame enter konid ...")
    
    elif choice == "2":
        print("Hazfe Daneshjoo")
        print("\n")
        
        name = input("Naame daneshjoo ra vared konid: ")
        stiudent_score = None
        for stiudent, score in zip(stiudents, scores):
            if stiudent == name:
                stiudents.remove(name)
                scores.remove(score)
                stiudent_score = score
                break

        else:
            print("Daneshjoo yaft nashod!")
            input("Baraie edame enter konid ...")
            continue

        print(f"Daneshjoo ba moshakhasate ro be ro hazf shod: {name} - {stiudent_score}")
        input("Baraie edame enter konid ...")

    elif choice == "3":
        print("Viraieshe Daneshjoo")
        print("\n")
        
        name = input("Naame daneshjoo ra vared konid: ")
        score_index = None
        for stiudent, score in zip(stiudents, scores):
            if stiudent == name:
                score_index = scores.index(score)
                break

        else:
            print("Daneshjoo yaft nashod!")
            input("Baraie edame enter konid ...")
            continue

        new_score = float(input("Nomre jadide daneshjoo ra vared konid: "))
        scores[score_index] = new_score
        print(f"Daneshjoo ba moshakhasate ro be ro viraiesh shod: {name} - {new_score}")
        input("Baraie edame enter konid ...")

    elif choice == "4":
        print("Namaieshe Daneshjooha")
        print("\n")
        for stiudent, score in zip(stiudents, scores):
            print(f"Name:\t {stiudent} | Score:\t {score}")

        print("\n")
        input("Baraie edame enter konid ...")
        pass

    elif choice == "5":
        print("Etmame barnameh.")
        break

    else:
        print("Entekhab eshtebah!")
        input("Baraie edame enter konid ...")    