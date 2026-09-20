class Solution:
    def transformStr(self, s: str, strs: List[str]) -> List[bool]:
        n=len(s)

        s1,s0=s.count('1'),s.count('0')
        ans=[]

        for t in strs:
            t1,t0,tq=t.count('1'),t.count('0'),t.count('?')
            if t1  > s1 or t0 > s0:
                ans.append(False)
                continue

            # prefix |t 1's| <= |s 1's|
            ct1=cs1=0
            flag=True
            for i in range(n):
                if s[i] == '1':
                    cs1+=1
                if t[i] == '1':
                    ct1+=1
                if ct1 > cs1:
                    flag=False
                    break
            
            # suffix |t 0's| <= |s 0's|
            ct0=cs0=0
            for i in range(n-1,-1,-1):
                if s[i] == '0':
                    cs0+=1
                if t[i] == '0':
                    ct0+=1
                if ct0 > cs0:
                    flag=False
                    break

            ans.append(flag)

        return ans
