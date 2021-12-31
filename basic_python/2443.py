# 별 찍기 6
row = int(input())

for i in range(row):
    print(' ' * i + '*' * (2 * (row - i) - 1))