class Solution:
    def getSum(self, nums: List[int]) -> int:
        arr = [0,0]
        for i in nums:
            arr.append(i)
            arr.append(0)
        arr.append(0)
        N=len(arr)

        prefix = [0]
        for i in arr: prefix.append(prefix[-1]+i)
        range_sum = lambda l,r: prefix[r+1]-prefix[l]

        p=[0]*N
        center=right=0
        mx=0

        for i in range(1,N-1):
            mirror = 2*center - i
            if i < right:
                p[i]=min(right-i,p[mirror])
            while i+1+p[i]<N and i-1-p[i]>=0 and arr[i+1+p[i]] == arr[i-1-p[i]]:
                p[i]+=1
            if i+p[i] > right:
                center,right=i,i+p[i]
            mx=max(mx,range_sum(i-p[i],i+p[i]))
        
        return mx
