# Найти сумму чисел списка, стоящих на нечетной позиции



def sum_odd_index(lst):
    s += [i for i in (len(lst)) if i % 2 == 0]
    for i in range(len(lst)):
        if i % 2 != 0:
            s += lst[i]
    print(f"Сумма равна: {s}")

lst = list(map(int, input("Введите числа через пробел:\n").split()))
sum_odd_index(lst)

# Старое решение:

# from random import randint

# def get_list(n, first, last):
#     return [randint(first, last) for i in range(n)]

# def sum_odd_position(mylist):
#     return sum(mylist[1::2])

# n = 10
# first = 1
# last = 10

# mylist = get_list(n, first, last)
# print(mylist)
# print(sum_odd_position(mylist))