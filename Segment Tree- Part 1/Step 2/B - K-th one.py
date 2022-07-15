# Submission Link: https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/submission/164137521

# https://codeforces.com/contest/1108/submission/48856997
# https://codeforces.com/blog/entry/18051
# https://codeforces.com/blog/entry/15890
# https://codeforces.com/blog/entry/15729


from math import log2, ceil
from sys import stdin
from bisect import bisect_left as bl
from collections import defaultdict

input = stdin.readline
read = lambda: map(int, input().strip().split())


def left(idx):
    return 2 * idx


def right(idx):
    return 2 * idx + 1


class SegmentTree:
    # Build Tree
    def __init__(self, arr):
        self.size = len(arr)
        self.tree_size = 2 ** self.size.bit_length()
        self.tree = [0] * 2 * self.tree_size
        for idx in range(self.size):
            self.tree[self.tree_size + idx] = arr[idx]
        for idx in reversed(range(1, self.tree_size)):
            self.tree[idx] = self.tree[left(idx)] + self.tree[right(idx)]
        self.idx, self.left_node, self.right_node = [1, 0, self.size - 1]

    def update(self, pos):
        start = self.tree_size + pos
        self.tree[start] ^= 1
        start //= 2
        while start:
            self.tree[start] = self.tree[left(start)] + self.tree[right(start)]
            start //= 2

    def query(self, k):
        idx = 1
        while idx < self.tree_size:
            if self.tree[left(idx)] >= k:
                idx = left(idx)
            else:
                k -= self.tree[left(idx)]
                idx = right(idx)
        return idx - self.tree_size


n, m = read()
lst = list(read())
st = SegmentTree(lst)
for x in range(m):
    q = list(read())
    if q[0] == 1:
        st.update(q[1])
    else:
        print(st.query(q[1] + 1))
