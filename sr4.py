def main(**kwargs):
    for i, j in kwargs.items():
        summ = sum(j) / len(j)
        print(summ)

if __name__ == '__main__':
    main(x=[1, 4, 5], y=[7, 8, 9])
