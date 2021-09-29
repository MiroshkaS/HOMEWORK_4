import math

print("Введите координаты точки")
x = float(input("x = "))
y = float(input("y = "))
r = float(input("r = "))

r_xy = math.sqrt(x ** 2 + y ** 2)

if r_xy <= r:
    print("Точка принадлежит кругу")
else:
    print("Точка не принадлежит кругу")