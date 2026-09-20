class Solution:
    def maxConsistentColumns(self, grid: List[List[int]], limit: int) -> int:
        m,n=len(grid),len(grid[0])

        def check(c1,c2):
            for i in range(m):
                if abs(grid[i][c2]-grid[i][c1]) > limit: return False
            return True
        
        arr=[[False]*n for _ in range(n)]

        for c1 in range(n):
            for c2 in range(c1+1,n):
                arr[c1][c2]=arr[c2][c1]=check(c1,c2)

        
        dp=[1]*n

        mx=0

        for r in range(n):

            for l in range(r):
                if arr[l][r]:
                    dp[r]=max(dp[r],1+dp[l])
            mx=max(mx,dp[r])
        
        return mx
