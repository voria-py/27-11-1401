# t.me/amirkho_eng
# GitHub: amirkho-py
# تابعی بنویسید که یک رشته به عنوان ورودی دریافت کند
# اگر تعداد حروف بزرگ آن بیشتر از حروف کوچک بود کل رشته را با حروف بزرگ برگرداند
# در غیر این صورت کل رشته را با حروف کوچک برگرداند




def capitalize_string(string:str):
    
    if sum(1 for c in string if c.isupper()) > len(string) / 2:
        return string.upper()
    else:
        return string.lower()


print(capitalize_string("HeLLO"))

