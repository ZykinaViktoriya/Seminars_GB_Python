# Задача 1. За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

# import math
# n = 700
# m = 750
# day = m / n
# print(math.ceil(day))

n = 700
m = int(input("Введите длину маршрута: "))
day = (m - 1 + n) // n
print(day)