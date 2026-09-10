from math import log2,ceil,floor

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    freq=[0]*(m+1)
    s=0
    for i in map(int,input().split()):
        freq[i]+=1
        s+=i

    suff = [0] * (m + 2)
    for val in range(m, 0, -1):
        suff[val] = suff[val + 1] + freq[val]

    max_k = m.bit_length()
    ans = [0] * m

    for k in range(1, m + 1):
        limit = 1 << k
        if limit >= m:
            ans[k-1] = s
            continue

        best = 0

        for L in range(1, ceil(m//limit)+1):
            curr = 0

            # Exact power-of-two bonus: carrots == 2^k * L
            exact_val = limit * L
            if exact_val <= m:
                curr += freq[exact_val]

            # Accumulate pieces for multiples: 1*L, 2*L, ..., (2^k - 1)*L
            for mult in range(1, limit):
                pos = mult * L
                if pos > m:
                    break
                curr += suff[pos]

            if curr > best:
                best = curr

        ans[k-1] = best

    print(*ans)
