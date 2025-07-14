# برنامه ای بنویسید که مقادیر a, b, c را از کاربر بگیرد و نتایج عبارات زیر را محاسبه و نمایش دهد:
# عبارت اول:  (a+b*c)<(a*b-c)or(a/b+c)>=(a*b/c)
# عبارت دوم:  not (a>b) and (b==c) or (a+b!=c)
# عبارت سوم:  (a**b>c) and (a//b<c) or not (a%b==c)

print()

a = float(input("Lotfan meghdar a ra vared konid: "))
b = float(input("Lotfan meghdar b ra vared konid: "))
c = float(input("Lotfan meghdar c ra vared konid: "))

expr1 = (a + b * c) < (a * b - c) or (a / b + c) >= (a * b / c)
expr2 = not (a > b) and (b == c) or (a + b != c)
expr3 = (a ** b > c) and (a // b < c) or not (a % b == c)
print("-" * 20)
print(f"Ebaret 1: (a + b * c) < (a * b - c) or (a / b + c) >= (a * b / c)")
print(f"Ebaret 2:  not (a > b) and (b == c) or (a + b != c)")
print(f"Ebaret 3: (a ** b > c) and (a // b < c) or not (a % b == c)")
print("-" * 20)
print(f"Ebaret 1: {expr1}")
print(f"Ebaret 2: {expr2}")
print(f"Ebaret 3: {expr3}")