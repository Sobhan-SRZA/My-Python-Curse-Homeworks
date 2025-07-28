# ▪ برنامه ای بنویسید که چند رشته را از ورودی گرفته و موارد زیر را بر روی آنها اعمال کند.
# ▪ متدهای پایه رشته ها )count ,()split ,()lower ,()upper ))(
# ▪ بررسی و یژگی های رشته ) isalnum ,()islower ,()isupper ))(
# ▪ برش رشته ها )slicing )
# ▪ جایگزین ی و تغییر متن
# ▪ کار با رشتهها به صورت لی ست
# ▪ تولید رشته های تصادفی
# ▪ فرمتدهی رشته ها.

print("Tamrin Shomare 8")
print("\n")

while True:
    string_count = input("Che tedad reshte mikhay vared koni? ")
    if not string_count.isdigit():
        print("Khata: Lotfan faghat adad vared konid!")
        continue
    string_count = int(string_count)
    break

# Gheyre az list, chare digei baraye zakhire vojood nadare
all_strings = []

i = 0
while i < string_count:
    s = input(f"Reshte shomare {i + 1} ra vared konid: ")
    all_strings += [s]
    i += 1

index = 0
while index < string_count:
    selected_string = all_strings[index]
    print(f"\n--- Reshte shomare {index + 1} ---")
    print("Matn asli: " + selected_string)

    # count
    print("Tedad harf 'a': " + str(selected_string.count('a')))

    # split
    print("Joda shode ba space:", selected_string.split())

    # lower / upper
    print("Be horoof koochik:", selected_string.lower())
    print("Be horoof bozorg:", selected_string.upper())

    # isalnum, islower, isupper
    print("Faghat horoof va adad?", selected_string.isalnum())
    print("Hame horoof koochike?", selected_string.islower())
    print("Hame horoof bozorg?", selected_string.isupper())

    # slicing
    print("3 harf aval:", selected_string[:3])
    print("3 harf akhar:", selected_string[-3:])
    print("Az harf 2 ta 5:", selected_string[2:5])

    # replace
    print("Jaye 'a' ba '*':", selected_string.replace('a', '@'))

    # tabdil be list
    chars = list(selected_string)
    print("Be list karakter:", chars)

    # format dahi
    print("Format dahi: Reshte-ye {} ba tool-e {} karakter.".format(selected_string, len(selected_string)))
    print(f"Estefade az f-string: reshte {index + 1} ba tool-e {len(selected_string)}")

    index += 1