"1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь."

def check(start, end, x):
    end = end + 1
    while True:
        try:
            text = '{} {} {} '.format("Введите", x, '')
            n = int(input(text))            
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")    
        else:
            if start <= n < end:
                return n
            print("Введённое число вне диапазона от 100 до 999")
            
def repit():
    while True:
            print("Желаете посчитать ещё числа? Да/Нет")
            answer = str(input("Ваше решение: "))
            if answer.lower() == "да":
                main()
            elif answer.lower() == "нет":
                print("Спасибо за использование нашего приложения!")
                break
            elif answer == " ":
                break
            else:
                print("Некорректный ввод.")
                continue
            
name_Of_user = input("Введите имя: ")

print ('Привет,', name_Of_user,'!')
print ('Пожалуйста, введите числа, которые хотите сложить!')
            
def main():
    first_number = check(100, 999, 'первое трёхзначное число: ')
    second_number = check(100, 999, 'второе трёхзначное число: ')
    summa_Of_numbers = first_number + second_number
    print("Сумма Ваших чисел,", name_Of_user, ":", summa_Of_numbers)
    
    
    
main()
repit()
    
