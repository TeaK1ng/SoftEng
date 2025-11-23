# Тема 11. Итераторы и генераторы
Отчет по Теме #11 выполнил:
- Шарипов Артур Айратович
- ПИЭ-23-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | # |
| Задание 4 | + | # |
| Задание 5 | + | # |


## Лабораторная работа №1
### Простой итератор, но у него нет гибкой настройки, например его нельзя развернуть. Он работает просто как next(), но нет prev()

```python
from functools import lru_cache

@lru_cache(None)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    print (fibonacci(100))
```
### Результат.
![1](https://github.com/TeaK1ng/SoftEng/blob/Tema_11/pic/1.jpg)

## Выводы




## Лабораторная работа №2
### Класс итератор с гибкой настройкой и удобными применением

```python
def check(input_func):
    def output_func(*args):
        name, age = args[0], args[1]

        if age < 0 or age > 130:
            age = 'Недопустимый возраст'
        input_func(name, age)

    return output_func

@check
def personal_info(name, age):
    print(f"Name: {name} Age: {age}")

if __name__ == '__main__':
    personal_info('Владимир', 38)
    personal_info('Александр', -5)
    personal_info('Петр', 138, 15, 48, 2)
```
### Результат.
![2](https://github.com/TeaK1ng/SoftEng/blob/Tema_11/pic/2.jpg)

## Выводы




## Лабораторная работа №3
### Генератор списка

```python
def data(*args):
    try:
        for i in range(len(*args)):
            try:
                result = (args[0][i] * 15) // 10
                print(result)
            except Exception as ex:
                print(ex)
    except Exception as ex:
        print(ex)
    finally:
        print('Вся информация обработана')

if __name__ == '__main__':
    data([1, 15, 'Hello', 'i', 'try', 'to', 'crash', 'your', 'site', 38, 45])
```
### Результат.
![3](https://github.com/TeaK1ng/SoftEng/blob/Tema_11/pic/3.jpg)

## Выводы




## Лабораторная работа №4
### Выражения генераторы

```python
class NegativValueException(Exception):
    pass

def check_name(name):
    if len(name) > 10:
        raise NegativValueException('Длина более 10 символов')
    else:
        print('Успешная регистрация')

if __name__ == '__main__':
    name = '12345678910'
    check_name(name)
```
### Результат.
![4](https://github.com/TeaK1ng/SoftEng/blob/Tema_11/pic/4.jpg)

## Выводы





## Лабораторная работа №5
### Такой же счетчик, как и в первом задании, только это генератор и использует yield

```python
class SiteChecker:
    def __init__(self, func):
        print('> Класс SiteChecker метод __init__ успешный запуск')
        self.func = func

    def __call__(self):
        print('> Проверка перед запуском', self.func.__name__)
        self.func()
        print('> Проверка безопасного выключения')


@SiteChecker
def site():
    print('Усердная работа сайта')

if __name__ == '__main__':
    print('>> Сайт запущен')
    site()
    print('>> Сайт выключен')
```
### Результат.
![5](https://github.com/TeaK1ng/SoftEng/blob/Tema_11/pic/5.jpg)

## Выводы
