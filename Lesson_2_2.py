n = int(input("Введите число: "))
even = odd = 0
while n > 0:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
    n = n // 10
print("Чётных - %d, Нечётных - %d" % (even, odd))