# ▪ برنامه ای بنویسید که چند رشته را از ورودی گرفته و موارد زیر را بر روی آنها اعمال کند.
# ▪ متدهای پایه رشته ها )count ,()split ,()lower ,()upper ))(
# ▪ بررسی و یژگی های رشته ) isalnum ,()islower ,()isupper ))(
# ▪ برش رشته ها )slicing )
# ▪ جایگزین ی و تغییر متن
# ▪ کار با رشتهها به صورت لی ست
# ▪ تولید رشته های تصادفی
# ▪ فرمتدهی رشته ها.
print("------ Barname Modiriat Reshte-ha ------\n")

while True:
    tedad = input("Che tedad reshte mikhahid vared konid? ")
    if not tedad.isdigit():
        print("Lotfan faghat adad vared konid.")
        continue

    tedad = int(tedad)
    break

reshtaha = []

i = 0
while i < tedad:
    r = input("Reshte ra vared konid: ")
    reshtaha.append(r)
    i += 1

while True:
    print("\n--- Menu Asli ---")
    print("1. Namayesh hameye reshtaha")
    print("2. Estefade az metod haye split/lower/upper/count")
    print("3. Barrasi isalnum / islower / isupper")
    print("4. Slicing roye reshte")
    print("5. Taghir matn ya jaygozini")
    print("6. Tabdil reshte be list")
    print("7. Tolide reshte tasadofi (az harf haye reshtaha)")
    print("8. Formatdehi reshte")
    print("9. Khorooj")

    entekhab = input("Yek gozine ra entekhab konid: ")

    if entekhab == "1":
        index = 0
        while index < len(reshtaha):
            print("Reshte", index + 1, "->", reshtaha[index])
            index += 1

        input("\nBaraie edameh enter konid...")
    

    elif entekhab == "2":
        print("Metod ra entekhab konid:")
        print("1. split")
        print("2. lower")
        print("3. upper")
        print("4. count")
        m = input("Shomare metod ra vared konid: ")
        shomare = input("Shomare reshte (az 1 ta {}) ra vared konid: ".format(len(reshtaha)))
        if shomare.isdigit() and int(shomare) <= len(reshtaha):
            reshte = reshtaha[int(shomare)-1]
            if m == "1":
                print("Natije split:", reshte.split())
                input("\nBaraie edameh enter konid...")

            elif m == "2":
                print("Natije lower:", reshte.lower())
                input("\nBaraie edameh enter konid...")

            elif m == "3":
                print("Natije upper:", reshte.upper())
                input("\nBaraie edameh enter konid...")

            elif m == "4":
                harf = input("Harf ya kalame baraye shomar vared konid: ")
                print("Tedad:", reshte.count(harf))
                input("\nBaraie edameh enter konid...")

            else:
                print("Gozine na motabar")
                input("\nBaraie edameh enter konid...")

        else:
            print("Shomare eshtebah ast")
            input("\nBaraie edameh enter konid...")

    elif entekhab == "3":
        shomare = input("Shomare reshte (az 1 ta {}) ra vared konid: ".format(len(reshtaha)))
        if shomare.isdigit() and int(shomare) <= len(reshtaha):
            reshte = reshtaha[int(shomare)-1]
            print("isalnum:", reshte.isalnum())
            print("islower:", reshte.islower())
            print("isupper:", reshte.isupper())

        else:
            print("Shomare eshtebah ast")
            input("\nBaraie edameh enter konid...")

    elif entekhab == "4":
        shomare = input("Shomare reshte (az 1 ta {}) ra vared konid: ".format(len(reshtaha)))
        if shomare.isdigit() and int(shomare) <= len(reshtaha):
            reshte = reshtaha[int(shomare)-1]
            az = input("Az kodam index shoro shavad? (0 shoroo): ")
            ta = input("Ta kodam index boro? ")
            if az.isdigit() and ta.isdigit():
                print("Hasil:", reshte[int(az):int(ta)])
                input("\nBaraie edameh enter konid...")

            else:
                print("Index ha bayad adad bashand.")
                input("\nBaraie edameh enter konid...")

        else:
            print("Shomare eshtebah ast")
            input("\nBaraie edameh enter konid...")


    elif entekhab == "5":
        shomare = input("Shomare reshte (az 1 ta {}) ra vared konid: ".format(len(reshtaha)))
        if shomare.isdigit() and int(shomare) <= len(reshtaha):
            reshte = reshtaha[int(shomare)-1]
            ghadimi = input("Kalame ghadimi: ")
            jadid = input("Kalame jadid: ")
            reshtaha[int(shomare)-1] = reshte.replace(ghadimi, jadid)
            print("Reshte jadid:", reshtaha[int(shomare)-1])
            input("\nBaraie edameh enter konid...")

        else:
            print("Shomare eshtebah ast")
            input("\nBaraie edameh enter konid...")


    elif entekhab == "6":
        shomare = input("Shomare reshte (az 1 ta {}) ra vared konid: ".format(len(reshtaha)))
        if shomare.isdigit() and int(shomare) <= len(reshtaha):
            reshte = reshtaha[int(shomare)-1]
            liste_horoof = []
            i = 0
            while i < len(reshte):
                liste_horoof.append(reshte[i])
                i += 1
            print("Reshte be list:", liste_horoof)
            input("\nBaraie edameh enter konid...")

        else:
            print("Shomare eshtebah ast")
            input("\nBaraie edameh enter konid...")

    elif entekhab == "7":
        print("Tedad horoof baraye estefade az string haye mojood ra vared konid:")
        tedad = input("Tedad horoof: ")
        if not tedad.isdigit():
            print("Lotfan adad vared konid.")
            input("\nBaraie edameh enter konid...")

        else:
            tedad = int(tedad)
            reshte = ""
            i = 0
            while i < tedad:
                sr = reshtaha[i % len(reshtaha)]
                reshte += sr[i % len(sr)]
                i += 1
            print("Reshte tasadofi:", reshte)
            input("\nBaraie edameh enter konid...")

    elif entekhab == "8":
        shomare = input("Shomare reshte (az 1 ta {}) ra vared konid: ".format(len(reshtaha)))
        if shomare.isdigit() and int(shomare) <= len(reshtaha):
            reshte = reshtaha[int(shomare)-1]
            print("Reshte format shode: [{}]".format(reshte))
            input("\nBaraie edameh enter konid...")

        else:
            print("Shomare eshtebah ast")
            input("\nBaraie edameh enter konid...")

    elif entekhab == "9":
        print("Khorooj az barname.")
        break

    else:
        print("Gozine na motabar ast.")