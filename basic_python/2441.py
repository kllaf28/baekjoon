# 별 찍기 4
row = int(input())

for i in range(row):
    print(' ' * i + '*' * (row - i))