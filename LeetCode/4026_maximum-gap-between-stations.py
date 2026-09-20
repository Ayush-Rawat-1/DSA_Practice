class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        n=len(skill)
        m=len(station)

        arr=[0]*m
        i,j=n-1,m-1

        while i>=0 and j>=0:
            if skill[i] == station[j]:
                arr[i]=j
                i-=1
            j-=1
        
        i=0
        res=0
        for j in range(m):
            if skill[i] == station[j] and i+1<n:
                res=max(res,arr[i+1]-j)
                i+=1
        
        return res
                
