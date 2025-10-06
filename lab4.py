def main(x, *args):
    one = x
    two = sum(args)
    three = float(len(args))
    print(f'one = {one}, two = {two}, three = {three}')

    return x + two / three


if __name__ == "__main__":
    res = main(10, 0, 1, 2, -1, 0, -1, 1, 2)
    print(f"result = {res}")
    
