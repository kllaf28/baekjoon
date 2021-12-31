# 별 찍기 2
row = int(input())

for i in range(row):
    print(' ' * (row - i - 1) + '*' * (i + 1))