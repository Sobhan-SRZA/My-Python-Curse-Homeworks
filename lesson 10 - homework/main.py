# .1 تابعی بنو یسید که یک رشته بگیرد و تعداد حروف صدادار )u ,o ,i ,e ,a )در آن را بشمارد.
# .2 تعداد کلمات به کار رفته در آن رشته را نشان دهد.
# .3 برخی از قواعد نگارشی همچون نقطه یا : یا ؟ گذاشتن در پایان جمله را به کاربر هشدار دهد.
def count_vowels(text):
    count = 0
    for i in text.lower():
        if i in ("a","e","i","o","u"):
            count += 1

    return count

    # return sum(1 for i in text.lower() if i in ("a","e","i","o","u"))

def count_words(text):
    return len(text.split())

def check_punctuation(text):
    if not text.strip().endswith((".",":","!","?")):
        return "Jomle shoma naghes ast!"

    return "Jomle shoma dorost tamam shode ast."


text = input("Matni jahate barrasi vared konid: ")

print("0. Matn vorodi:", text)
print("1. Tedad horofe seda dar:", count_vowels(text))
print("2. Tedad kalamat:", count_words(text))
print("3. Barrasi etmame jomle:", check_punctuation(text))