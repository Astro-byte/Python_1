"""8. Определить, является ли год, 
который ввел пользователем, високосным или невисокосным."""

def check(start, end, x):
    end = end + 1
    while True:
        try:
            text = '{} {} {} '.format("Введите", x, ":")
            n = int(input(text))            
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")    
        else:
            if start <= n < end:
                return n
            print("Из введённого числа нельзя составить треугольник! Попробуйте снова:")
            

year = check(1, 4000, 'год, чтобы узнать, високосный он или нет')

if ((year % 4 == 0) and not (year % 100 == 0)) or (year % 400 == 0):
    print("Високосный")
else:    
    print("Невисокосный")
