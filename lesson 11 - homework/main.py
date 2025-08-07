# تاپلی را برای کدگذاری معین کرده و با دریافت یک رشته از کاربر استفاده از تابعی رشته را کدگذاری و با تابع دیگری آنرا کدگشایی نمائید

code_table = (
    ("q","£"),
    ("w","5"),
    ("e",":"),
    ("r","6"),
    ("t","7"),
    ("y","9"),
    ("u","0"),
    ("i","@"),
    ("o","1"),
    ("p","2"),
    ("a","3"),
    ("s","%"),
    ("d","'"),
    ("f","\""),
    ("g","4"),
    ("h","8"),
    ("j","#"),
    ("k","-"),
    ("l",","),
    ("z","?"),
    ("x",";"),
    ("c","!"),
    ("v","\\"),
    ("b","^"),
    ("n","&"),
    ("m","_"),
    (" ","=")
)


def encode(text):
    for orjinalLetter, replacementLetter in code_table:
       text = text.replace(orjinalLetter, replacementLetter)
        
    return text
    
def decode(text):
    for orjinalLetter, replacementLetter in code_table:
       text = text.replace(replacementLetter, orjinalLetter)
        
    return text
    
    
text = input("Lotfan matne vorodi ra vared konid: ")

print("orjinal text:", text)
print("encoded text:", encode(text))
print("decoded text:", decode(text))
