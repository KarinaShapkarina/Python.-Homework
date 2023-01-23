# Найти произведение пар чисел в списке.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


def mult_lst(lst):
    l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
    my_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    print(my_lst)

lst = list(map(int, input("Введите числа через пробел:\n").split()))
mult_lst(lst)

# Старое решение:

# from random import randint
# import math

# def get_list(n, first, last):
#     return [randint(first, last) for i in range(n)]

# def mult_nums(mylist):
#     return [mylist[i] * mylist[-i - 1] for i in range(math.ceil(len(mylist)/2))]

# n = 9
# first = 1
# last = 10

# mylist = get_list(n, first, last)
# print(mylist)
# print(mult_nums(mylist))