class Solution:
    def createGrid(self, m: int, n: int, k: int) -> list[str]:
        arr=[[0]*n for _ in range(m)]

        r=c=-1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j == n-1:
                    arr[i][j]=1
                if i < m-1:
                    arr[i][j]+=arr[i+1][j]
                if j<n-1:
                    arr[i][j]+=arr[i][j+1]
                if arr[i][j] == k:
                    r,c=i,j
                    break
                if i+1<m and j+1<n and arr[i+1][j+1]*2 == k:
                    r,c=i,j
                    break
        
        if r == -1:
            return []
        
        grid=[['#']*n for _ in range(m)]

        if arr[r][c] == k:
            for i in range(r,m):
                for j in range(c,n):
                    grid[i][j]='.'
            
            for i in range(r+1):
                grid[i][0]='.'
            for j in range(c+1):
                grid[r][j]='.'
        else:
            for i in range(r+1,m):
                for j in range(c+1,n):
                    grid[i][j]='.'
            for i in range(r+1):
                grid[i][0]='.'
            for j in range(c+1):
                grid[r][j]='.'
            if r+1<m and c+1<n and arr[r+1][c+1] * 2 == k:
                grid[r+1][c]=grid[r][c+1]='.'
            else: return []

        
        return [''.join(row) for row in grid]
