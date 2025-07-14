# برنامه ای بنویسید که اعداد اول بین 1 تا 1000 را محاسبه و چاپ کند.
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        
    return True

try:
    number = int(input("addadi vared konid ta adade avale  bein 1 ta on adad chap shavad: "))
    
except ValueError:
    print("Faqat adad mored qabol ast!")

prime_nums = []
for n in range(1, number + 1):
    if is_prime(n):
        prime_nums.append(str(n))

    else:
        continue

prime_nums_len = len(prime_nums)
if prime_nums_len > 0:
    print("tedad adade aval: ", prime_nums_len)
    print("\t".join(prime_nums))

else:
    print("adade avai yaft nashod.")