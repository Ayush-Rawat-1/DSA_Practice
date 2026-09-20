from sortedcontainers import SortedList
class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        n=len(nums)
        for i in range(n):
            if nums[i]%2: nums[i]=a
            else: nums[i]=-b
        
        res=0
        pr=0

        sl = SortedList([0])
        # print(nums)

        for i in range(n):
            pr += nums[i]
            sl.add(pr)
            idx = bisect.bisect_right(sl,pr)-1
            res += idx

            # print(sl,pr,idx,res)
        return res
