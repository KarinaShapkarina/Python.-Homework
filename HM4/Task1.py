# Вычислить число c заданной точностью d. 
# Пример:
#     при d = 0.001,π = 3.141    10^(-1)≤d≤10^(-10).

from math import pi
def get_precision(f):
    str_f = str(f)
    if '.' not in str_f:
        return 0

    # Получение строки после точки и возвращение ее длины
    return len(str_f[str_f.index('.') + 1:])

d = float(input("Введите число для заданной точности числа Пи:\n"))

print(f'число Пи с заданной точностью {d} равно {round(pi, get_precision(d))}')


