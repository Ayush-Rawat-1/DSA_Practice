# Point update + Range Query
class BIT:
    def __init__(self, n, arr):
        ''' O(n) time by pushing each element's prefix sum directly to its immediate parent'''
        self.n = n
        self.bit = [0] * (self.n + 1)
        for i in range(n):
            idx = 1 + i  # 1-based indexing
            self.bit[idx] += arr[i]
            parent = idx + (idx & (-idx))
            if parent <= n:
                self.bit[parent] += self.bit[idx] 

    def update(self, idx, val):
        '''Adds value 'val' to 0-based index 'idx' '''
        idx += 1  # Convert to 1-based indexing
        while idx <= self.n: 
            self.bit[idx] += val
            idx += idx & (-idx)

    def get_sum(self, idx):
        '''Returns sum of prefix [0, idx] '''
        idx += 1  # Convert to 1-based indexing
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & (-idx)
        return s

    def range_sum(self, l, r):
        '''Returns sum of range [l, r] inclusive '''
        return self.get_sum(r) - self.get_sum(l - 1)

# Range Update + Point Query -> Using Difference Array
class RangeUpdatePointQueryBIT:
    def __init__(self,arr):
        self.n=len(arr)
        self.bit=[0]*(self.n+1)
        prev = 0
        ## D[0] = arr[0] & D[i] = arr[i]-arr[i-1]
        ##O(N)
        for i in range(self.n):
            idx = i + 1
            self.bit[idx] += arr[i] - prev
            parent = idx + (idx & -idx)
            if parent <= self.n:
                self.bit[parent] += self.bit[idx]
            prev = arr[i]
        ##O(Nlog(n))
        # for i in range(self.n):
        #     self._update(i,arr[i]-prev)
        #     prev=arr[i]

    def update(self,l,r,val):
        self._update(l,val)
        self._update(r+1,-val)

    def _update(self,idx,val):
        idx += 1
        while idx <= self.n:
            self.bit[idx] += val
            idx += idx & -idx

    def get_sum(self, idx):
        idx += 1
        s=0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & -idx
        return s

# Range Update + Range Query
class RangeUpdateRangeQueryBIT:
    def __init__(self, n, arr=None):
        self.n = n
        self.bit1 = [0] * (n + 1)
        self.bit2 = [0] * (n + 1)
        
        for i in range(n):
            self.range_update(i, i, arr[i])

    def _add(self, bit, idx, val):
        """Standard BIT point add on 1-based index."""
        while idx <= self.n:
            bit[idx] += val
            idx += idx & (-idx)

    def _query(self, bit, idx):
        """Standard BIT prefix sum on 1-based index."""
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & (-idx)
        return s

    def range_update(self, l, r, val):
        """Adds 'val' to all indices in [l, r] (0-based, inclusive)."""
        # Convert 0-based [l, r] to 1-based [L, R]
        L = l + 1
        R = r + 1

        # BIT1 updates: D[L] += val, D[R + 1] -= val
        self._add(self.bit1, L, val)
        self._add(self.bit1, R + 1, -val)

        # BIT2 updates: (D[L] * L) += val * L, (D[R + 1] * (R + 1)) -= val * (R + 1)
        self._add(self.bit2, L, val * L)
        self._add(self.bit2, R + 1, -val * (R + 1))

    def prefix_sum(self, idx):
        """Returns sum of arr[0...idx] (0-based)."""
        k = idx + 1  # Convert to 1-based index
        if k <= 0:
            return 0
        
        sum_bit1 = self._query(self.bit1, k)
        sum_bit2 = self._query(self.bit2, k)
        
        return (k + 1) * sum_bit1 - sum_bit2

    def range_query(self, l, r):
        """Returns sum of elements in range [l, r] (0-based, inclusive)."""
        return self.prefix_sum(r) - self.prefix_sum(l - 1)
