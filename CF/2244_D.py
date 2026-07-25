import math
 
def solve(n,m,A,B):
    prefix=[0]
    B.sort()
    for i in A:
        prefix.append(prefix[-1]+i)
    
    res=abs(prefix[B[0]])
    for i in range(1,m):
        res += abs(prefix[B[i]]-prefix[B[i-1]])
    res+=prefix[n]-prefix[B[m-1]]
    
    print(res)
    
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    solve(n,m,A,B)
