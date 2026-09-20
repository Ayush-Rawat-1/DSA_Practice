MOD = 10**9 + 7
max_n = 10**5

fact = [1] * (max_n + 1)
for i in range(1, max_n + 1):
    fact[i] = fact[i-1] * i % MOD

inv_fact = [1] * (max_n + 1)
inv_fact[max_n] = pow(fact[max_n], MOD - 2, MOD)
for i in range(max_n - 1, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

def comb(n, k):
    if n < 0 or k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD