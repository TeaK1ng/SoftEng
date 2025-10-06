def main(**kwargs):
    for i in kwargs.items():
        print(i[0], i[1])

    for key in kwargs:
        print(f'{key} = {kwargs[key]}')


if __name__ == "__main__":
    main(x=[1, 2, 3], y=[4, 5, 6], z=[7, 8, 9])

    print()

    main(**{'x': [1, 2, 3], 'y': [4, 5, 6]})
