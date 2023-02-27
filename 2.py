# t.me/amirkho_eng
# GitHub: amirkho-py
# تابعی بنویسید که لیستی از اعداد دریافت کند و بزرگترین عدد فرد را بازگرداند
# استفاده از توابع آماده مجاز نیست




def max_odd_num(numbers:list):

    max_odd = numbers[0]
    
    for num in numbers:
        if num > max_odd and num%2 != 0:
            max_odd = num
    
    return max_odd



print(max_odd_num([13,2,1,135,6,8,9,0]))


