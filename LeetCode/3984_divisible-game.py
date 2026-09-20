N=10**6 + 1
primes = [True]*N
primes[0]=primes[1]=False
fact = [[] for _ in range(N)]

p=0

while p*p <= N:
    if primes[p]:
        fact[p].append(p)
        for j in range(p+p,N,p):
            primes[j]=False
            fact[j].append(p)
    p+=1

class Solution:
    def divisibleGame(self, nums: list[int]) -> int:
        INF=float('-inf')
        res=(INF,0)
        n=len(nums)

        for num in nums:
            if primes[num] and not fact[num]:
                fact[num].append(num)

        for i in range(n):
            s=0
            mx,k=0,2
            mpp=defaultdict(int)
            for j in range(i,n):
                s+=nums[j]
                for f in fact[nums[j]]:
                    mpp[f]+=nums[j]
                    if mpp[f]>mx or (mpp[f]==mx and f<k):
                        mx=mpp[f]
                        k=f
                x=2*mx-s
                
                if x>res[0] or (x==res[0] and k<res[1]):
                    res=(x,k)
        
        MOD=10**9 + 7

        return (res[0]*res[1])%MOD
