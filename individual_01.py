import math

x1 = float(input("x1: "))
y1 = float(input("y1: "))

abs_x1 = abs(x1)
abs_y1 = abs(y1)

arith_mean = (abs_x1 + abs_y1) / 2
geom_mean = math.sqrt(abs_x1 * abs_y1)

print(f"Среднее арифметическое модулей: {arith_mean:.2f}")
print(f"Среднее геометрическое модулей: {geom_mean:.2f}")