class Node:
    def __init__(self, row_id, row):
        self.id = row_id
        self.row = row
        self.prev = None
        self.next = None

class Table:
    def __init__(self, cols):
        self.cols = cols
        self.cur_id = 1
        self.lookup = {}
        self.head = Node(-1, [])
        self.tail = Node(-1, [])
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, row):
        if len(row) != self.cols:
            return False
        node = Node(self.cur_id, row)
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node
        self.lookup[self.cur_id] = node
        self.cur_id += 1
        return True

    def delete(self, row_id):
        node = self.lookup.pop(row_id, None)
        if not node:
            return
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, row_id, col_idx):
        if row_id in self.lookup and 0 <= col_idx < self.cols:
            return self.lookup[row_id].row[col_idx]
        return None

    def export_all(self):
        curr = self.head.next
        out = []
        while curr is not self.tail:
            out.append(f"{curr.id}," + ",".join(curr.row))
            curr = curr.next
        return out

class SQL:
    def __init__(self, names, columns):
        self.db = {n: Table(c) for n, c in zip(names, columns)}

    def ins(self, name, row):
        return self.db[name].add(row) if name in self.db else False

    def rmv(self, name, rowId):
        if name in self.db:
            self.db[name].delete(rowId)

    def sel(self, name, rowId, columnId):
        if name not in self.db:
            return "<null>"
        val = self.db[name].get(rowId, columnId - 1)
        return "<null>" if val is None else val

    def exp(self, name):
        return self.db[name].export_all() if name in self.db else []
