MAX=21
fact=[0]*MAX
  
def probability(k, n): 
    ans = 0
    for i in range(k,n+1): 
        ans += fact[n] / (fact[i] * fact[n - i])  
    # 1 << n = pow(2, n) 
    ans = ans / (1 << n) 
    return ans 
  
def precompute(): 
  
    fact[0] = 1
    fact[1] = 1
  
    for i in range(2,20): 
        fact[i] = fact[i - 1] * i 
  
if __name__=='__main__': 
    precompute() 
    n = int(input("Enter tosses (max 19): "))
    N = int(input("Enter heads in a row: "))
    if (N <= n):
        if (n <= 19):
            chance = probability(N, n)
            print("Probability of getting ", N, " heads in ", n, " tosses is ", chance)
        else:
            print("Cant toss more than 19 coins.")
    else:
        print("You cant get more Heads than the number of tosses your doing.")
