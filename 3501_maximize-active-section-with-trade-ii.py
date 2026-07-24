class SegmentTree:
    # max segment tree
    def __init__(self,arr):
        self.n=len(arr)
        if self.n == 0: return
        self.tree=[0]*(4*self.n)
        self.build(0,0,self.n-1,arr)
    
    def build(self,idx,s,e,arr):
        if s == e:
            self.tree[idx]=arr[s]
            return
        mid=(s+e)//2
        left,right=2*idx+1,2*idx+2
        self.build(left,s,mid,arr)
        self.build(right,mid+1,e,arr)
        self.tree[idx]=max(self.tree[left],self.tree[right])
    
    def range(self,l,r):
        if l>r: return 0
        return self._range(0,0,self.n-1,l,r)
    
    def _range(self,idx,s,e,l,r):
        if r<s or e<l: return 0
        if l<=s and e<=r: return self.tree[idx]
        mid=(s+e)//2
        left,right=2*idx+1,2*idx+2

        return max(self._range(left,s,mid,l,r), self._range(right,mid+1,e,l,r))


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n=len(s)
        ones=[]
        zeros=[]
        o=0
        z=0
        to=0

        for i in range(n):
            if s[i] == '1':
                to+=1
                o+=1
                z=0
                if o == 1:
                    ones.append([i,i])
                else:
                    ones[-1][1]=i
            else:
                o=0
                z+=1
                if z == 1:
                    zeros.append([i,i])
                else:
                    zeros[-1][1]=i
        

        extras=[]
        Z,O=len(zeros),len(ones)
        for i in range(Z-1):
            extras.append(zeros[i][1]-zeros[i][0]+1+zeros[i+1][1]-zeros[i+1][0]+1)
        
        # print(zeros)
        # print(ones,to)
        # print(extras)

        seg=SegmentTree(extras)

        def bs_l(arr,x):
            l,r=0,len(arr)-1

            while l<=r:
                mid=(l+r)//2
                if arr[mid][1] >= x:
                    r=mid-1
                else:
                    l=mid+1
            
            return r+1
        
        def bs_r(arr,x):
            l,r=0,len(arr)-1

            while l<=r:
                mid=(l+r)//2
                if arr[mid][0] <= x:
                    l=mid+1
                else:
                    r=mid-1
            
            return l-1
        
        ans=[]

        for s,e in queries:
            lidx,ridx=bs_l(zeros,s),bs_r(zeros,e)
            if Z == lidx:
                ans.append(to)
                continue
            l=lidx+1 if s > zeros[lidx][0] else lidx
            r=ridx-1 if e < zeros[ridx][1] else ridx
            ex = seg.range(l,r-1)
            # print(lidx,ridx,l,r,ex)

            if lidx == ridx:
                ex=0
            elif lidx+1 == ridx:
                ex = max(ex, zeros[lidx][1]-max(s,zeros[lidx][0])+1 + min(e,zeros[ridx][1])-zeros[ridx][0]+1)
            else:
                if lidx != l and lidx < Z-1:
                    ex = max(ex, zeros[lidx][1]-max(s,zeros[lidx][0])+1 + zeros[lidx+1][1]-zeros[lidx+1][0]+1)
                if ridx != r and ridx>0:
                    ex = max(ex, zeros[ridx-1][1]-zeros[ridx-1][0]+1 + min(e,zeros[ridx][1])-zeros[ridx][0]+1)
            
            # print(to,ex)
            ans.append(to+ex)


        return ans
