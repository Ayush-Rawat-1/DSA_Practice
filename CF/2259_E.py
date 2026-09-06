

def solve(n,arr):
    line=[0]*(n+1)
    for i in range(n):
        if arr[i] <= 0: continue
        l=max(0,i-arr[i]+1)
        r=min(n,i+arr[i])
        line[l]+=1
        line[r]-=1
    x=0
    res=['0']*n
    for i in range(n):
        x+=line[i]
        if x == 0:
            res[i]='1'
    for i in range(n):
        if arr[i] == -1: continue
        if not ((i-arr[i]>=0 and res[i-arr[i]] == '1') or (i+arr[i]<n and res[i+arr[i]] == '1')):
            print("-1")
            return
    print(''.join(res))


t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    
    solve(n,arr)
