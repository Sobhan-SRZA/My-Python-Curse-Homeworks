# ▪ برنامه ای بنویسید که چند رشته را از ورودی گرفته و موارد زیر را بر روی آنها اعمال کند.
# ▪ متدهای پایه رشته ها )count ,()split ,()lower ,()upper ))(
# ▪ بررسی و یژگی های رشته ) isalnum ,()islower ,()isupper ))(
# ▪ برش رشته ها )slicing )
# ▪ جایگزین ی و تغییر متن
# ▪ کار با رشتهها به صورت لی ست
# ▪ تولید رشته های تصادفی
# ▪ فرمتدهی رشته ها.

print("Tamrin Shomare 8")
print("\n\n")

string_count=None

while True:
    string_count = input("Che tedad reshte vared mikonid? ")
    if not string_count.isdigit():
        print("Khata: Faqat adade morede qabol ast!")
        continue

    string_count = int(string_count)
    break

