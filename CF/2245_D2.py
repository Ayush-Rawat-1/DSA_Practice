import math
from collections import deque

t=int(input())  

def solve(n,m,edges):
    arr=[[0,0] for _ in range(n)]
    graph=[[] for _ in range(n)]
    
    for o,u,v in edges:
        arr[u][o]+=1
        arr[v][o]+=1
        graph[u].append((v,o))
        graph[v].append((u,o))
        
    q=deque()
    vis=[False]*n
    for u in range(n):
        if arr[u][0] == 0 or arr[u][1] == 0:
            vis[u]=True
            q.append(u)
    
    dirs=[]
    while q:
        u=q.popleft()
        if arr[u][0] == 0:
            dirs.append((u,-1))
        else:
            dirs.append((u,1)) 
        for v,o in graph[u]:
            arr[v][o]-=1
            if arr[v][o] == 0 and not vis[v]:
                vis[v]=True
                q.append(v)
    
    if len(dirs) < n:
        print("NO")
        return
    res=[0]*n
    dirs.reverse()
    for i in range(n):
        res[dirs[i][0]]=(i+1)*dirs[i][1]
    
    print("YES")
    print(*res)

for _ in range(t):
    n,m=map(int,input().split())
    edges=list(tuple(map(int,input().split())) for _ in range(m))
    edges=[(o-1,u-1,v-1) for o,u,v in edges]
    solve(n,m,edges)
