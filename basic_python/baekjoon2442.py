# 별 찍기 5
row = int(input())

for i in range(row):
    print(' ' * (row - i - 1) + '*' * (2 * i + 1))