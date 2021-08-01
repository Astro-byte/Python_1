"""1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, 
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный 
и отсортированный массивы. Сортировка должна быть реализована в виде функции. 
По возможности доработайте алгоритм (сделайте его умнее)."""

import random


def bubble(lst):
    n = 1

    while n < len(lst):
        count = 0

        for i in range(len(lst) - 1 - (n - 1)):

            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                count += 1

        if count == 0:
            break

        n += 1


amount = 11
lesser = -100
more = 99
array = [random.randint(lesser, more) for _ in range(amount)]

print('Входные данные:', array, sep='\n')
bubble(array)
print('Полученные данные после сортировки:', array, sep='\n')