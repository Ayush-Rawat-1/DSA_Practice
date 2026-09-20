class Solution:
    def minInitialStrength(self, monsters: list[int], boosts: list[list[int]]) -> int:
        n=len(monsters)
        line=[0]*(n+1)

        for l,r,v in boosts:
            line[l]+=v
            line[r+1]-=v
        r=-1
        b=0
        res=0
        for i in range(n):
            b+=line[i]
            line[i]=b
            if b < monsters[i]:
                r=i
        
        return 0 if r == -1 else sum(monsters[:r+1])-line[r]
