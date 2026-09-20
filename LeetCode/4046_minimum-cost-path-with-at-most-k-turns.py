class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        valid=lambda x,y: 0<=x<m and 0<=y<n
        dirs=((-1,0),(1,0),(0,-1),(0,1))
        
        dis=[[[[float('inf')]*4 for _ in range(k+1)] for _ in range(n)] for _ in range(m)]
        
        pq = [(grid[0][0],0,0,k,t) for t in range(4)]
        
        for t in range(4):
            dis[0][0][k][t]=grid[0][0]
    
        while pq:
            cost,i,j,k,turn = heapq.heappop(pq)
            if dis[i][j][k][turn] != cost:
                continue
            if i == m-1 and j == n-1:
                return cost
            for t in range(4):
                di,dj=dirs[t]
                ni,nj=i+di,j+dj
                nk=k
                if turn != t:
                    nk-=1
                
                if valid(ni,nj) and nk>=0 and dis[ni][nj][nk][t]>cost+grid[ni][nj]:
                    # vis[ni][nj][nk]=True
                    dis[ni][nj][nk][t]=cost+grid[ni][nj]
                    heapq.heappush(pq,(cost+grid[ni][nj],ni,nj,nk,t))

        return -1
