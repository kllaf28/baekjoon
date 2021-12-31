from sys import stdin, stdout

a, b = map(int, input().split())
k_lst = [int(x) for x in stdin.readline().rstrip().split()]
total = 0

for i in range(a + 1):
    if i == 0 or i == 1:
        continue
    
    for k in k_lst:
        if i % k == 0:
            total += i
            break
    
print(total)
