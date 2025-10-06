from datetime import datetime #импортируем модуль datetime
from math import sqrt #импортируем модуль math

def main(**kwargs): #создаем функцию и передаем в нее ключевые аргументы
    for key in kwargs.items(): #перебираем ключ для key
        res = sqrt(key[1][0] ** 2 + key[1][1] ** 2) #достаём числа из списка и возводим их в степень, а далее получаем корень
        print(res) #выводим результат в консоль

if __name__ == '__main__': #точка входа
    start_time = datetime.now() #в переменную записываем время до выполнения
    main(
        one=[10, 3],
        two=[5, 4],
        three=[15, 13],
        four=[93, 53],
        five=[133, 15]
    ) #передаем в функцию аргументы
    time_costs = datetime.now() - start_time #вычисляем время работы функции
    print(f"Время выполнения программы - {time_costs}") #выводим в консоль
