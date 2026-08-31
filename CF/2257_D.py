import math
def solve(s,q):
    fact=[]
    for i in range(1,math.floor(math.sqrt(s)+1)):
        if s%i == 0:
            fact.append((i,s//i))
    fact += [(j,i) for i, j in fact if i!=j][::-1]
    n=len(fact)
    pre = [0]
    prev=0
    for i,j in fact:
        pre.append(pre[-1]+j*(i-prev))
        prev=i

    def prefix(l,r):
        if l > r: return 0
        return pre[r+1]-pre[l]

    def bs(x):
        l,r=0,n-1
        while l <= r:
            mid=(l+r)//2
            if x >= fact[mid][0]:
                l=mid+1
            else:
                r=mid-1
        return l-1

    def bs2(y):
        l,r=0,n-1
        while l <= r:
            mid=(l+r)//2
            if y >= fact[mid][1]:
                r=mid-1
            else:
                l=mid+1
        return r+1

    # print(fact)
    # print(pre)
    for _ in range(q):
        x,y=map(int,input().split())
        res=0
        l,r=bs2(y),bs(x)
        # print((x,y),(l,r))
        if l <= r:
            res = prefix(l+1,r)
            if l == 0:
                res += fact[l][0]*fact[l][1]
            else:
                res += fact[l-1][0]*min(y,fact[l-1][1]) + (fact[l][0]-fact[l-1][0])*fact[l][1]
            if r < n-1:
                res += (min(s,x)-fact[r][0])*min(y,fact[r+1][1])
        else:
            res = fact[r][0]*min(y,fact[r][1]) + (min(s,x)-fact[r][0])*min(y,fact[r+1][1])
        print(res)

t=int(input())

for _ in range(t):
    s,q=map(int,input().split())
    solve(s,q)
