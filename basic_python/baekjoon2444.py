# 별 찍기 7
row = int(input())


for i in range(row):
    print(' ' * (row - i - 1) + '*' * (2 * i + 1))

for i in range(row - 1):
    print(' ' * (i + 1) + '*' * (2 * (row - (i + 1)) - 1))