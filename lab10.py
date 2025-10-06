global res
def rectangle():
    a = float(input("Ширина: "))
    b = float(input("Высота: "))
    global res
    res = a * b

def triangle():
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    global res
    res = 0.5 * a * h

figure = input("1-прямоугольник, 2-треугольник: ")

if figure == "1":
    rectangle()
elif figure == "2":
    triangle()

print(f"Площадь: {res}")
