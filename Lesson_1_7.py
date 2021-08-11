"""7. По длинам трех отрезков, введенных пользователем, 
определить возможность существования треугольника, составленного из этих отрезков. 
Если такой треугольник существует, то определить, является ли он разносторонним, 
равнобедренным или равносторонним."""



def check(start, end, x):
    end = end + 1
    while True:
        try:
            text = '{} {} {} '.format("Введите", x, "=")
            n = int(input(text))            
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")    
        else:
            if start <= n < end:
                return n
            print("Из введённого числа нельзя составить треугольник! Попробуйте снова:")
            

side_a = check(1, 40, 'сторону а')
side_b = check(1, 40, 'сторону b')
side_c = check(1, 40, 'сторону c')


if side_a != side_b and side_b != side_c and side_c != side_a:
    print("Этот треугольник разносторонний.")
elif side_a == side_b and side_b == side_c and side_c == side_a:
    print("Этот треугольник равносторонний.")
elif side_a == side_b or side_b == side_c or side_c == side_a:
    print("Этот треугольник равнобедренный.")
    