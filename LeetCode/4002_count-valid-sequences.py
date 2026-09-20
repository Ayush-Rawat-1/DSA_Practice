MOD=10**9 + 7
N=5*pow(10,5)
fact = [1]*(N+1)
ifact = [1]*(N+1)
for i in range(2,N+1):
    fact[i]=(fact[i-1]*i)%MOD
ifact[-1] = pow(fact[-1],-1,MOD)
for i in range(N-1,1,-1):
    ifact[i] = (i+1)*ifact[i+1]%MOD

def comb(n,k):
    if n<k or k<0: return 0
    return ((fact[n] * ifact[n-k]) % MOD * ifact[k]) % MOD

class Solution:
    def countValidSequences(self, n: int, k: int) -> int:
        # Total ways with Sum n and Length k
        T = comb(n-1,k-1)

        # Total ways with all odd elements
        if (n+k)%2 == 0:
            O = comb(((n+k)//2) - 1,k-1)
        else:
            """
            If sum is odd, length is even then no way,
            If sum is even, length is odd then no way
            thus if (Sum + length) % 2 == 1: then No way to form a sequence with all odd elements
            """
            O=0

        return (T-O+MOD)%MOD


"""
Stars and bars to compute Total ways with sum S and length N
comb(S-1, N-1)

Atleast one even element should be present = Total ways - All odds ways

All odds ways,
Sum = S and length = N
x1 + x2 ... + xn = S, xi = +ve odd
x = 2*y - 1 where y>=1

y1+y2+...+yn = (S+N)/2

"""
