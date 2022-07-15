# Sorted List: https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/submission/164251558


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

    def update(self, pos, new_val):
        start = self.tree_size + pos
        self.tree[start] = new_val
        start //= 2
        while start:
            self.tree[start] = self.tree[left(start)] + self.tree[right(start)]
            start //= 2

    def range_sum(self, range_left, range_right):
        sum = 0
        range_left += self.tree_size
        range_right += self.tree_size
        while range_left <= range_right:
            if range_left & 1:
                sum += self.tree[range_left]
                range_left += 1
            if not range_right & 1:
                sum += self.tree[range_right]
                range_right -= 1
            range_right //= 2
            range_left //= 2
        return sum


n = int(input())
st = SegmentTree([0] * (n + 1))
for idx, el in enumerate(read()):
    st.update(el, 1)
    print(st.range_sum(el + 1, n), end=" ")
