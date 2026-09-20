
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
        idx = idx + 1  # Convert to 1-based indexing
        while idx <= self.n: 
            self.bit[idx] += val
            idx += idx & (-idx)

    def get_sum(self, idx):
        '''Returns sum of prefix [0, idx] '''
        idx = idx + 1  # Convert to 1-based indexing
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & (-idx)
        return s

    def range_sum(self, l, r):
        '''Returns sum of range [l, r] inclusive '''
        return self.get_sum(r) - self.get_sum(l - 1)