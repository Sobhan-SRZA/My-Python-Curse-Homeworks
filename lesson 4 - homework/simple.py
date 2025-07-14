# برنامه ای بنویسید که دو عدد و یک عملگر (+و -و *و /) دریافت کند و عملیات مربوطه را انجام دهد.

vorodi1 = float(input("Lotfan adad avval ra vared konid: "))
vorodi2 = float(input("Lotfan adad dovvom ra vared konid: "))
amaliat = input("Lotfan amalgar (+, -, *, /) ra vared konid: ")

if amaliat == '+':
    natije = vorodi1 + vorodi2
    print(f"Natije: {vorodi1} + {vorodi2} = {natije}")

elif amaliat == '-':
    natije = vorodi1 - vorodi2
    print(f"Natije: {vorodi1} - {vorodi2} = {natije}")

elif amaliat == '*':
    natije = vorodi1 * vorodi2
    print(f"Natije: {vorodi1} * {vorodi2} = {natije}")

elif amaliat == '/':
    if vorodi2 == 0:
        print("Khata: Taghsim bar sefr!")

    else:
        natije = vorodi1 / vorodi2
        print(f"Natije: {vorodi1} / {vorodi2} = {natije}")
        
else:
    print("Amalgar namotabar ast!")