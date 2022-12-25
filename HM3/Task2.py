# Найти произведение пар чисел в списке.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint
import math

def get_list(n, first, last):
    return [randint(first, last) for i in range(n)]

def mult_nums(mylist):
    return [mylist[i] * mylist[-i - 1] for i in range(math.ceil(len(mylist)/2))]

n = 9
first = 1
last = 10

mylist = get_list(n, first, last)
print(mylist)
print(mult_nums(mylist))