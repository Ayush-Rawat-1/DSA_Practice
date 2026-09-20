class Solution:
    def interleaveCharacters(self, word1: str, word2: str, target: str) -> int:
        n1,n2,m=len(word1),len(word2),len(target)
        MOD=10**9 + 7
        
        dp=[[1]*(n2+1) for _ in range(n1+1)]
        for i1 in range(n1+1):
            dp[i1][0]=0 
        for i2 in range(1,n2+1): 
            dp[0][i2]=0

        for j in range(m-1,-1,-1):
            ndp=[[0]*(n2+1) for _ in range(n1+1)]
            for i1 in range(n1,-1,-1):
                suffix = [0]*(n2+1)
                for i2 in range(n2-1,-1,-1):
                    if word2[i2] == target[j]:
                        suffix[i2]=suffix[i2+1]+dp[i1][i2+1]
                    else:
                        suffix[i2]=suffix[i2+1]
                for i2 in range(n2,-1,-1):
                    ndp[i1][i2] = (ndp[i1][i2]+suffix[i2])%MOD
            
            for i2 in range(n2,-1,-1):
                suffix = [0]*(n1+1)
                for i1 in range(n1-1,-1,-1):
                    if word1[i1] == target[j]:
                        suffix[i1]=suffix[i1+1]+dp[i1+1][i2]
                    else:
                        suffix[i1]=suffix[i1+1]
                for i1 in range(n1,-1,-1):
                    ndp[i1][i2] = (ndp[i1][i2]+suffix[i1])%MOD
            dp=ndp
        
        ans=dp[0][0]
        return ans
