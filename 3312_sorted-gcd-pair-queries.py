class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        n=len(nums)
        freq = Counter(nums)
        mx=max(nums)
        left=n*(n-1)//2

        arr=[0]*(mx+1)

        gcds=[]

        for i in range(mx,1,-1):
            curr=ex=0
            for j in range(i,mx+1,i):
                curr += freq[j]
                ex += arr[j]
            pairs = curr*(curr-1)//2 - ex
            left -= pairs
            arr[i]=pairs
            if pairs:
                gcds.append((i,pairs))
        
        if left:
            gcds.append((1,left))
        
        gcds=gcds[::-1]

        N=len(gcds)
        prefix=[0]*N
        prefix[0]=gcds[0][1]
        for i in range(1,N):
            prefix[i]=prefix[i-1]+gcds[i][1]

        # print(gcds)
        # print(prefix)

        res=[]

        for idx in queries:
            i=bisect.bisect_left(prefix,idx+1)
            res.append(gcds[i][0])

        return res
