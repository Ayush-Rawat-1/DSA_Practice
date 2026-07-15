class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)
        if n>m: return False
        if n == 1: return True

        front=[-1]*n
        back=[-1]*n

        i=0
        for j in range(m):
            if s[i] == t[j]:
                front[i]=j
                i+=1
            if i == n:
                return True
        
        i=n-1
        for j in range(m-1,-1,-1):
            if s[i] == t[j]:
                back[i]=j
                i-=1
            if i==-1:
                return True
        
        if (back[1]!=-1 and back[1] > 0) or (front[n-2]!=-1 and front[n-2] < m-1):
            return True
        
        for i in range(1,n-1):
            if front[i-1] != -1 and back[i+1] != -1 and back[i+1]-front[i-1]>=2: return True
        
        return False
