with open('input.txt', 'a+') as f:
    f.write('\nЯ дополнительная строка')

with open('input.txt', 'r') as f:
    result = f.readlines()
    print(result)