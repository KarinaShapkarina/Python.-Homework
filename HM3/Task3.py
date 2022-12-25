# В заданном списке вещественных чисел найдите разницу 
# между максимальным и минимальным значением дробной части элементов

from random import uniform


def get_list(n, first, last):
    return [round(uniform(first,last), 2) for i in range(n)]

def find_nums(mylist):
    nums = [round(x - int(x), 2) for x in (mylist)]
    return max(nums) - min(nums)

n = 5
first = 1
last = 5

mylist = get_list(n, first, last)
print(mylist)
print(find_nums(mylist))