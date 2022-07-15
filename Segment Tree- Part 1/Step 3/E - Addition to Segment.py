# Submission Link: https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/submission/164143934

# https://codeforces.com/contest/1108/submission/48856997
# https://codeforces.com/blog/entry/18051
# https://codeforces.com/blog/entry/15890
# https://codeforces.com/blog/entry/15729


from math import log2, ceil
from sys import stdin
from bisect import bisect_left as bl
from collections import defaultdict
from array import array

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

    def range_update(self, range_left, range_right, val):
        range_left += self.tree_size
        range_right += self.tree_size
        while range_left <= range_right:
            if range_left & 1:
                self.tree[range_left] += val
                range_left += 1
            if not range_right & 1:
                self.tree[range_right] += val
                range_right -= 1
            val <<= 1
            range_right //= 2
            range_left //= 2

    def query(self, pos):
        idx = (pos + self.tree_size) >> 1
        path = []
        while idx:
            path.append(idx)
            idx >>= 1
        for idx in reversed(path):
            self.tree[left(idx)] += self.tree[idx] >> 1
            self.tree[right(idx)] += self.tree[idx] >> 1
            self.tree[idx] = 0
        return self.tree[pos + self.tree_size]


n, m = read()
st = SegmentTree([0] * (n + 5))
for x in range(m):
    q = list(read())
    if q[0] == 1:
        st.range_update(q[1], q[2] - 1, q[3])
    else:
        print(st.query(q[1]))
