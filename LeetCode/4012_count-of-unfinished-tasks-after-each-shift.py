class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        n=len(tasks)
        m=len(shifts)
        prefix = tasks[:]
        for i in range(1,n):
            prefix[i]+=prefix[i-1]
        
        res=[0]*m
        curr=0
        
        for i in range(m):
            done = bisect.bisect_left(prefix,curr+shifts[i]+1)
            res[i] = n-done
            if done == n: curr=0
            else: curr+=shifts[i]
        
        return res
