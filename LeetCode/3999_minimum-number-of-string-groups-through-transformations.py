P=31
MOD=999999929
power=[1]
for i in range(500000):
    power.append(power[-1]*P % MOD)

class Solution:
    def minimumGroups(self, words: List[str]) -> int:
        both=set()
        res=0

        # char to int
        cti=lambda x: ord(x)-ord('a')+1

        for idx in range(len(words)):
            s=words[idx]
            n=len(s)
            es=[s[i] for i in range(0,n,2)]
            m=len(es)
            es += es[:m-1]
            h=0
            eh=float('inf')
            
            for i in range(len(es)):
                h = (h*P + cti(es[i])) % MOD
                if i >= m:
                    h = (h - cti(es[i-m])*power[m] + MOD) % MOD
                if i>=m-1:
                    eh=min(eh,h)
        
            os=[s[i] for i in range(1,n,2)]
            m=len(os)
            h=0
            os += os[:m-1]
            oh=float('inf')
            for i in range(len(os)):
                h = (h*P + cti(os[i])) % MOD
                if i >= m:
                    h = (h - cti(os[i-m])*power[m] + MOD) % MOD
                if i>=m-1:
                    oh=min(oh,h)

            both.add((eh,oh))
        
        return len(both)
