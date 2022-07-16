# Submission Link: https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/submission/164543953

# Dictionary == Hash Collision

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


def cal(a, b, mod):
    return [(a[0] * b[0] + a[1] * b[2]) % mod, (a[0] * b[1] + a[1] * b[3]) % mod,
            (a[2] * b[0] + a[3] * b[2]) % mod, (a[2] * b[1] + a[3] * b[3]) % mod]


class SegmentTree:
    # Build Tree
    def __init__(self, arr, mod):
        self.size = len(arr)
        self.mod = mod
        self.tree_size = 2 ** (self.size - 1).bit_length()
        self.tree = [[1, 0, 0, 1] for i in range(2 * self.tree_size)]
        for idx in range(self.size):
            self.tree[self.tree_size + idx] = arr[idx]
        for idx in reversed(range(1, self.tree_size)):
            self.tree[idx] = cal(self.tree[left(idx)], self.tree[right(idx)], self.mod)
        # print(self.tree[1:])

    def range_sum(self, range_left, range_right):
        left = [1, 0, 0, 1]
        right = [1, 0, 0, 1]
        range_left += self.tree_size
        range_right += self.tree_size
        while range_left <= range_right:
            if range_left & 1:
                left = cal(left, self.tree[range_left], self.mod)
                range_left += 1
            if not range_right & 1:
                right = cal(self.tree[range_right], right, self.mod)
                range_right -= 1
            range_right //= 2
            range_left //= 2
        sum = cal(left, right, self.mod)
        print(*sum[:2])
        print(*sum[2:])
        print()


r, n, m = read()
lst = [0] * n
for i in range(n):
    lst[i] = read() + read()
    input()
# print(lst)
st = SegmentTree(lst, r)
for x in range(m):
    q = list(read())
    st.range_sum(q[0] - 1, q[1] - 1)
