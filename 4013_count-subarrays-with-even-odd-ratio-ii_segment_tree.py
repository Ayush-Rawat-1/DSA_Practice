class SegmentTree:
    def __init__(self,n):
        self.n=n
        self.tree=[0]*(4*self.n)

    def update(self,idx,val):
        self._update(0,0,self.n-1,idx,val)
    
    def _update(self,i,s,e,idx,val):
        if s == e:
            self.tree[i]=val
            return
        mid=(s+e)//2
        left,right=2*i+1,2*i+2
        if idx <= mid:
            self._update(left,s,mid,idx,val)
        else:
            self._update(right,mid+1,e,idx,val)
        self.tree[i] = self.tree[left] + self.tree[right]

    def range(self,l,r):
        return self._range(0,0,self.n-1,l,r)
    
    def _range(self,i,s,e,l,r):
        if r<s or e<l:
            return 0
        if l<=s and e<=r: 
            return self.tree[i]
        mid=(s+e)//2
        left,right=2*i+1,2*i+2
        return self._range(left,s,mid,l,r) + self._range(right,mid+1,e,l,r)


class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        n=len(nums)
        for i in range(n):
            if nums[i]%2: nums[i]=a
            else: nums[i]=-b
        
        res=0
        prefix=[(0,0)]

        for i in range(n):
            prefix.append((prefix[-1][0]+nums[i],i+1))

        idxs = {j:i for i,(_,j) in enumerate(sorted(prefix))}
        
        # print(idxs)
        # print(prefix)

        seg=SegmentTree(n+1)

        for _,i in prefix:
            seg.update(idxs[i],1)
            res += seg.range(0,idxs[i])-1

        return res
