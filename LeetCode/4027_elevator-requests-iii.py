class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[list[int]]) -> int:
        N=len(requests)
        full_mask = (1<<N)-1
        INF=float('inf')
        dp=[[INF]*N for _ in range(full_mask+1)]

        for i in range(N):
            dp[1<<i][i] = max(requests[i][0],abs(start-requests[i][1]))
        
        for mask in range(1,full_mask):
            for u in range(N):
                if ((mask&(1<<u)) == 0): continue
                t=dp[mask][u]
                for v in range(N):
                    if ((mask & (1<<v)) == 0):
                        dp[mask | (1<<v)][v] = min(dp[mask | (1<<v)][v],max(requests[v][0],t+abs(requests[u][1]-requests[v][1])))
        
        return min(dp[full_mask])
