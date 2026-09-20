import math

def solve(n,q,arr,queries):
    nums=list(sorted((v,i) for i,v in enumerate(arr)))
    res=0
    for i in range(n):
        j = nums[i][1]
        if i == j: continue
        for b in range(20,-1,-1):
            x=1<<b
            if (i&x) != (j&x):
                res=max(res,x)
                break
    print(res)
            
        
t=int(input())

for _ in range(t):
    n,q=map(int,input().split())
    arr=list(map(int,input().split()))
    queries=list(tuple(map(int,input().split())) for _ in range(q))
    solve(n,q,arr,queries)
