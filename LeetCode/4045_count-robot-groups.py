class Solution:
    def countGroups(self, position: list[int], speed: list[int], distance: int) -> int:
        n=len(position)
        if n == 1: return 1

        curr=speed[n-1]
        res=1
        for i in range(n-2,-1,-1):
            if position[i+1]-position[i] > distance:
                if curr >= speed[i]:
                    curr=speed[i]
                    res+=1
        
        return res
