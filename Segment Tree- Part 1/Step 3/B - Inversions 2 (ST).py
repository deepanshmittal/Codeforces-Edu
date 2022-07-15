# Submission Link: https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/submission/164319579

# Dictionary == Hash Collision
from array import array
from sys import stdin
from bisect import bisect_left as bl, bisect_right as br
from collections import defaultdict, Counter, deque


def input():
    return stdin.readline()


def read(default=int):
    return list(map(default, input().strip().split()))


def left(idx):
    return 2 * idx


def right(idx):
    return 2 * idx + 1


class SegmentTree:
    # Build Tree
    def __init__(self, arr):
        self.size = len(arr)
        self.tree_size = 2 ** self.size.bit_length()
        self.tree = array("i", [0] * 2 * self.tree_size)
        for idx in range(self.size):
            self.tree[self.tree_size + idx] = arr[idx]
        for idx in reversed(range(1, self.tree_size)):
            self.tree[idx] = self.tree[left(idx)] + self.tree[right(idx)]

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


def solve():
    n = read()[0]
    st = SegmentTree([1] * n)
    ans = [0] * n
    for idx, el in enumerate(reversed(read())):
        ans[idx] = st.query(n - idx - el) + 1
        st.update(ans[idx] - 1)
    return reversed(ans)


# t = int(input())
t = 1
for test in range(t):
    print(*solve())
