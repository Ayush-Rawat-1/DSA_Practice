import math

def solve(n,q,s,queries):
    prefix=[0]*n
    for i in range(n-1):
        prefix[i+1] = prefix[i] + int(s[i] == s[i+1])
    
    for l,r,k in queries:
        x = (prefix[r-1]-prefix[l-1]+1)//2
        if x<=k: print("YES")
        else: print("NO")
    
t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    s=input()
    queries=list(tuple(map(int,input().split())) for _ in range(q))
    solve(n,q,s,queries)
