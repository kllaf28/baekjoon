# 1로 만들기
memo = [0] * (10 ** 6 + 1)

memo[1] = 0
memo[2] = memo[3] = 1

n = int(input())


for i in range(4, n + 1):
    memo[i] = memo[i-1] + 1        
    
    if i % 3 == 0:
        memo[i] = min(memo[i//3] + 1, memo[i])
        
    if i % 2 == 0:
        memo[i] = min(memo[i//2] + 1, memo[i])
        
    #print(i, memo[i])
    

print(memo[n])

