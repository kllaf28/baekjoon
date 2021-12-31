# 별 찍기 8
row = int(input())


for i in range(row):
    print('*' * (i + 1) + 
          ' ' * (2 * (row - i - 1)) +
          '*' * (i + 1))

for i in range(row):
    if i == 0:
        continue
        
    print('*' * (row - i) + 
          ' ' * (2 * i) +
          '*' * (row - i))
