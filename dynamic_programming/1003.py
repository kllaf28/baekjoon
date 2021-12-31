#피보나치
memo = [0] * 41

def fibo_td(x):
    
    if x == 1 or x == 2:
        return 1
    
    if memo[x] != 0:
        return memo[x]
    
    memo[x] = fibo_td(x - 1) + fibo_td(x - 2)
    return memo[x]
    
memo[1] = 1
memo[2] = 1    
num_T = int(input())

for _ in range(num_T):
    num = int(input())
    if num == 0:
        print(1, 0)
        
    else:
        fibo_td(num)
        print(memo[num-1], memo[num])
    

    