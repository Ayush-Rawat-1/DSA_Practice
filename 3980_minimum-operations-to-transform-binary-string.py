class Solution:
    def minOperations(self, s1: str, s2: str) -> int:
        if s1 == s2: return 0
        n=len(s1)
        if n == 1:
            return 1 if s1=='0' else -1
            
        mpp={'00':0,'01':1,'10':2,'11':3}
        mat=[
            [0,1,1,2],
            [2,0,3,1],
            [2,3,0,1],
            [1,2,2,0]
        ]

        convert = lambda a,b: mat[mpp[a]][mpp[b]]

        INF=float('inf')
        
        dp=[INF,INF]
        dp[int(s2[n-1])]=0

        for i in range(n-1,-1,-1):
            ndp=[INF,INF]
            for prev in '01':
                res=INF
                if i == 0:
                    if s1[i] == '0':
                        res=min(res,1+dp[1])
                    res=min(res,dp[int(s1[i])])
                else:
                    if prev == s2[i-1]:
                        if s1[i] == '0':
                            res=min(res,1+dp[1])
                        res=min(res,dp[int(s1[i])])
                    res=min(
                        res,
                        convert(prev+s1[i], s2[i-1]+'0') + dp[0],
                        convert(prev+s1[i], s2[i-1]+'1') + dp[1],
                    )
                ndp[int(prev)]=res
            dp=ndp

        ans=dp[0]
        return ans if ans != INF else -1
