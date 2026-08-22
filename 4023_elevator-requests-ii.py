class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[int]) -> int:
        N=len(requests)
        prv,nxt=N-1,N
        curr=start
        requests.sort()

        for i in range(N):
            if requests[i] > start:
                prv=i-1
                nxt=i
                break
        
        @cache
        def go(prv,nxt,curr):
            res=float('inf')
            left = prv+1 + N-nxt
            if prv >= 0 and nxt < N:
                t1 =  (curr - requests[prv])*left
                res = min(res,t1+go(prv-1,nxt,requests[prv]))
                t2 = (requests[nxt]- curr)*left
                res = min(res,t2+go(prv,nxt+1,requests[nxt]))

            elif prv >= 0:
                res=0
                while prv >= 0:
                    time = (curr - requests[prv])*left
                    res += time
                    curr = requests[prv]
                    prv -= 1
                    left-=1
            elif nxt < N:
                res=0
                while nxt < N:
                    time = (requests[nxt] - curr)*left
                    res += time
                    curr = requests[nxt]
                    nxt += 1
                    left-=1
            else:
                res=0
            return res

        res = go(prv,nxt,curr)
        go.cache_clear()

        return res
