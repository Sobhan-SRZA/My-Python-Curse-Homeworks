# برنامه ای بنویسید که اعداد اول بین 1 تا 1000 را محاسبه و چاپ کند.
is_prime = True

print("adad avale bein 1 ta 1000")
for i in range(1, 1000 + 1):
    if i <= 1:
        is_prime = False
        continue

    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break

    else: 
        is_prime = True
    
    if is_prime:
        print(i)