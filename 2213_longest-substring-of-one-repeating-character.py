class SegmentTree:
    def __init__(self,st):
        self.n=len(st)
        self.tree=[[0]*6 for _ in range(4*self.n)]
        # 0:left_count, 1:right_count, 2:left_chr, 3:right_chr, 4:isSame, 5:Max_count
        self.build(0,0,self.n-1,st)
    
    def merge(self,i,left,right):
        if self.tree[left][3] == self.tree[right][2]:
            mid=self.tree[left][1]+self.tree[right][0]
            if self.tree[left][4]:
                self.tree[i][0]=mid
            else:
                self.tree[i][0]=self.tree[left][0]
            
            if self.tree[right][4]:
                self.tree[i][1]=mid
            else:
                self.tree[i][1]=self.tree[right][1]
            
            self.tree[i][2]=self.tree[left][2]
            self.tree[i][3]=self.tree[right][3]
            self.tree[i][4]=self.tree[left][4] & self.tree[right][4]
            self.tree[i][5]=max(mid,self.tree[left][5],self.tree[right][5])
        else:
            self.tree[i][0]=self.tree[left][0]
            self.tree[i][1]=self.tree[right][1]
            self.tree[i][2]=self.tree[left][2]
            self.tree[i][3]=self.tree[right][3]
            self.tree[i][4]=0
            self.tree[i][5]=max(self.tree[left][5],self.tree[right][5])
        

    def build(self,i,s,e,st):
        if s == e:
            self.tree[i][0]=self.tree[i][1]=1
            self.tree[i][2]=self.tree[i][3]=st[s]
            self.tree[i][4]=1
            self.tree[i][5]=1
            return
        mid=(s+e)//2
        left,right=2*i+1,2*i+2
        self.build(left,s,mid,st)
        self.build(right,mid+1,e,st)
        self.merge(i,left,right)

    def update(self,key,val):
        self._update(0,0,self.n-1,key,val)
    
    def _update(self,i,s,e,key,val):
        if s == e:
            self.tree[i][0]=self.tree[i][1]=1
            self.tree[i][2]=self.tree[i][3]=val
            self.tree[i][4]=self.tree[i][5]=1
            return
        mid=(s+e)//2
        left,right=2*i+1,2*i+2
        if key <= mid:
            self._update(left,s,mid,key,val)
        else:
            self._update(right,mid+1,e,key,val)
        self.merge(i,left,right)

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n=len(s)
        k=len(queryIndices)
        ordx = lambda x: ord(x)-ord('a')
        
        seg=SegmentTree(s)
        res=[]

        for key,val in zip(queryIndices,queryCharacters):
            seg.update(key,val)
            res.append(seg.tree[0][5])
            
        
        return res

