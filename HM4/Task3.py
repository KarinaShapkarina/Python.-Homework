# Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности.

from random import randint

def create_list(size, m, n):
    return [randint(m, n) for i in range(size)]


size = 10
m = 1
n = 10

origin = create_list(size, m, n)
print(origin)
a = []
b = []
[a.append(i) for i in origin]
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
        b.append(a[i])
        
print(b)
