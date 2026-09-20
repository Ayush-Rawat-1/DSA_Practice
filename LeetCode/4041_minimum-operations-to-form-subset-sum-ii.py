class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        n=len(nums)
        INF=float('inf')

        dp=[]

        for i in range(n):
            arr={}
            d,curr=0,nums[i]
            prev=0
            while curr > 0:
                if curr <= sum:
                    arr[curr]=min(arr.get(curr,INF),d)
                if d == 0 or prev != curr*2:
                    x,m=curr,d
                    while x<=sum:
                        arr[x]=min(arr.get(x,INF),m)
                        m+=1
                        x*=2
                prev=curr
                curr//=2
                d+=1
            dp.append(sorted(arr.items()))
        
        @cache
        def go(i,t):
            if t == 0:
                return 0
            if i == n:
                return INF
            
            res=go(i+1,t)
            
            for x,y in dp[i]:
                if x > t: break
                if y > res: continue
                res=min(res,y+go(i+1,t-x))
            
            return res
        
        res=go(0,sum)
        if res == INF:
            return -1
        
        # print(dp)
        
        return res
