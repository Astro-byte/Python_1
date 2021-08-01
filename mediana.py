"""3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
 Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
 в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы. 
 Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, 
 то используйте метод сортировки, который не рассматривался на уроках"""


import random


def median(lst, first, last):

    lst = lst.copy()
    ind = len(lst) // 2

    if first >= last:
        return lst[ind]

    pillar = lst[ind]
    i = first
    j = last

    while i <= j:

        while lst[i] < pillar:
            i += 1

        while lst[j] > pillar:
            j -= 1

        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1

    if ind < i:
        lst[ind] = median(lst, first, j)

    elif j < ind:
        lst[ind] = median(lst, i, last)

    return lst[ind]


def merger_sorting(arr):

    def merger(fst, snd):
        res = []
        i, j = 0, 0

        while i < len(fst) and j < len(snd):

            if fst[i] < snd[j]:
                res.append(fst[i])
                i += 1

            else:
                res.append(snd[j])
                j += 1

        res.extend(fst[i:] if i < len(fst) else snd[j:])

        return res

    def div_half(lst):

        if len(lst) == 1:
            return lst

        elif len(lst) == 2:
            return lst if lst[0] <= lst[1] else lst[::-1]

        else:
            return merger(div_half(lst[:len(lst)//2]), div_half(lst[len(lst)//2:]))

    return div_half(arr)


lesser = 0
more = 30
mini_size = 8
maximum_size = 11

m = random.randint(mini_size, maximum_size)
amount = 2 * m + 1

array = [random.randint(lesser, more) for _ in range(amount)]

# cProfile.run('median_search(array, 0, len(array) - 1)')

print(f'Сгенерирован массив из 2*{m}+1 = {amount}  элементов:', array, sep='\n')

median = median(array, 0, len(array) - 1)
print(f'Медиана: {median}')
# print(array, '\n')

print('Отсортированный массив: ', merger_sorting(array), sep='\n')
if median == merger_sorting(array)[len(array)//2]:
    print('\nВундерфуль')
else:
    print('\nНайн!!!')