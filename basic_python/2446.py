# 별 찍기 9
row = int(input())

for i in range(row):
    print(' ' * i + '*' * (2 * (row - i) - 1))

for i in range(row):
    if i == 0:
        continue
    print(' ' * (row - i - 1) + '*' * (2 * i + 1))

