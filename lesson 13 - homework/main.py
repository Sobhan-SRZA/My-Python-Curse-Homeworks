# تابعی بنو یسید به نام age_calculate که:
# o سال تولد کاربر را در یافت کند )عدد صح یح مثبت(
# o سن او را محاسبه کند )فرض کنید سال جاری 1404است(
# خطاهای ز یر را مدی ری ت کند:
# ورودی غیرعددی
# سال تولد بزرگتر از 1404
# سال تولد منف ی
# استفاده از استثنا ی سفارشی برای موارد خاص 
remain_year = 1404

class AgeCalculateError(Exception):
    pass

def age_calculate(age_year: str):
    try:
        age_year = int(age_year)
    except:
        raise AgeCalculateError("Khata: Vorody Adad nist!")

    if age_year >= remain_year:
        raise AgeCalculateError(f"Khata: Sen voroodi bozorg tar az {remain_year} ast! (Az ayande omadi!?)")
    
    age_number = remain_year - age_year

    if age_number < 1:
        raise AgeCalculateError(f"Khata: Sen koochektar az 1 shod!")

    return age_number
    
while True:
    try:
        print()
        print("Baraie khooroj \"exit\" type konid!")
        user_input = input("Sal tavallod ra vared konid: ")
        if user_input == "exit":
            print("Khodayafez.")
            break

        print(f"Sen mishavad: {age_calculate(user_input)}")
        print()

    except AgeCalculateError as e:
        print(e)
        input()