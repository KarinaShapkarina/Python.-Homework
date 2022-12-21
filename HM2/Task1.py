# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


number = float(input("Введите число: "))
a = int(number) 
b = number - int(number) 

sum = 0
while (a != 0): 
    sum = sum + (a % 10)
    a = a // 10
while (b != 0): 
    sum = sum + int(b*10) 
    b = b * 10 - int(b * 10)
print("Сумма цифр равна:", sum)