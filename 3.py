# t.me/amirkho_eng
# GitHub: amirkho-py
# تابعی بنویسید که یک عدد صحیح به عنوان ورودی دریافت کند و فاکتوریل آن را برگرداند



def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(5))