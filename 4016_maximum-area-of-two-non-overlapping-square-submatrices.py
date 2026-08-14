class Solution:
    def maxArea(self, mat: List[List[int]]) -> int:
        m,n=len(mat),len(mat[0])
        right=[list(mat[i]) for i in range(m)]
        down=[list(mat[i]) for i in range(m)]
        sq=[list(mat[i]) for i in range(m)]

        for i in range(1,m):
            for j in range(1,n):
                if mat[i][j] == 0: continue
                right[i][j]+=right[i][j-1]
                down[i][j]+=down[i-1][j]
                sq[i][j]+=min(sq[i-1][j-1],right[i][j-1],down[i-1][j])
        
        # print(sq)
        
        def go(k):
            arr=[[0]*n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if sq[i][j]>=k:
                        arr[i][j]+=1
                    if i>0:
                        arr[i][j]+=arr[i-1][j]
                    if j>0:
                        arr[i][j]+=arr[i][j-1]
                    if i>0 and j>0:
                        arr[i][j]-=arr[i-1][j-1]
                    
            for i in range(m):
                for j in range(n):
                    if sq[i][j]>=k and ((j>=k and arr[-1][j-k]) or (i>=k and arr[i-k][-1])):
                        return True
            return False

        l,r=1,min(m,n)
        res=0
        while l<=r:
            mid=(l+r)//2
            if go(mid):
                res=mid
                l=mid+1
            else:
                r=mid-1
        
        return res*res
