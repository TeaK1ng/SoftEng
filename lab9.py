from datetime import datetime as dt
from datetime import timedelta as td

def main():
    print(
        f'сегодня {dt.today().date()}'
        f'день недели {dt.today().isoweekday()}'
    )

    n = int(input("Введите число:"))
    today = dt.today()
    res = today + td(days=n)

    print(
        f'через {n} дней будет {res.date()} '
        f'день недели - {res.isoweekday()}'
    )

if __name__ == '__main__':
    main()
