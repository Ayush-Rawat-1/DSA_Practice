MAX = 10**5
seive=list(range(MAX+1))
p=2

while p*p <= MAX:
    if seive[p] == p:
        for j in range(p*p,MAX+1,p):
            seive[j]=min(p,seive[j])
    p+=1

class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        def prime_factors(num):
            factors=set()
            while num > 1:
                factors.add(seive[num])
                num//=seive[num]
            return factors
        
        n=len(nums)
        arr=[prime_factors(num) for num in nums]

        res=l=0
        freq=Counter()
        cnt=0

        for r in range(n):
            for num in arr[r]:
                freq[num]+=1
                if freq[num] == 1: cnt+=1
            
            while cnt > k:
                for num in arr[l]:
                    freq[num]-=1
                    if freq[num] == 0: cnt-=1
                l+=1
            
            res=max(res,r-l+1)
        
        return res
