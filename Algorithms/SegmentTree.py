class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)  # Segment tree array
        self.lazy = [0] * (4 * self.n)  # Lazy propagation array
        self.build(arr, 0, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        if start == end:
            # Leaf node will have a single element
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.build(arr, left_child, start, mid)
            self.build(arr, right_child, mid + 1, end)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def propagate(self, node, start, end):
        if self.lazy[node] != 0:
            # Apply the pending updates to the current node
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                # Not a leaf node, propagate the update to the children
                left_child = 2 * node + 1
                right_child = 2 * node + 2
                self.lazy[left_child] += self.lazy[node]
                self.lazy[right_child] += self.lazy[node]
            # Clear the lazy value at current node
            self.lazy[node] = 0

    def range_sum(self, L, R):
        return self._range_sum(0, 0, self.n - 1, L, R)

    def _range_sum(self, node, start, end, L, R):
        self.propagate(node, start, end)
        if R < start or end < L:
            return 0
        if L <= start and end <= R:
            return self.tree[node]
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        left_sum = self._range_sum(left_child, start, mid, L, R)
        right_sum = self._range_sum(right_child, mid + 1, end, L, R)
        return left_sum + right_sum

    def range_update(self, L, R, value):
        self._range_update(0, 0, self.n - 1, L, R, value)

    def _range_update(self, node, start, end, L, R, value):
        self.propagate(node, start, end)
        if R < start or end < L:
            return
        if L <= start and end <= R:
            # Apply the update to this segment
            self.lazy[node] += value
            self.propagate(node, start, end)
            return
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        self._range_update(left_child, start, mid, L, R, value)
        self._range_update(right_child, mid + 1, end, L, R, value)
        self.tree[node] = self.tree[left_child] + self.tree[right_child]
    
    def point_query(self, index):
        return self._point_query(0, 0, self.n - 1, index)

    def _point_query(self, node, start, end, index):
        self.propagate(node, start, end)

        if start == end:
            # Reached the target index
            return self.tree[node]

        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        if index <= mid:
            return self._point_query(left_child, start, mid, index)
        else:
            return self._point_query(right_child, mid + 1, end, index)
