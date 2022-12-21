# Реализуйте алгоритм перемешивания списка.


n = int(input("Введите размер списка: "))
spam = list(range(1, n + 1))
print(spam)
import random  
random.shuffle(spam) 
print(spam)
