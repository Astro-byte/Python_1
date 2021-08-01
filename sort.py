"""2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
заданный случайными числами на промежутке [0; 50). 
Выведите на экран исходный и отсортированный массивы."""

import random

amount = 11
array = [random.uniform(0, 50) for i in range(amount)]
print(array)


def sort(a):
    if len(a) < 2:
        return a
    left = sort(a[:len(a) // 2])
    right = sort(a[len(a) // 2:len(a)])

    q = r = s = 0

    while q < len(left) and r < len(right):
        if left[q] < right[r]:
            a[s] = left[q]
            q = q + 1
        else:
            a[s] = right[r]
            r = r + 1
        s = s + 1

    while q < len(left):
        a[s] = left[q]
        q = q + 1
        s = s + 1

    while r < len(right):
        a[s] = right[r]
        r = r + 1
        s = s + 1
    return a


print(sort(array))