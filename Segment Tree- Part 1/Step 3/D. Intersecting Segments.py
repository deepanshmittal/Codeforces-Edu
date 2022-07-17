# Submission Link: https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/submission/164644230
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
        self.tree_size = 2 ** (self.size - 1).bit_length()
        self.tree = [0] * 2 * self.tree_size
        for idx in range(self.size):
            self.tree[self.tree_size + idx] = arr[idx]
        for idx in reversed(range(1, self.tree_size)):
            self.tree[idx] = self.tree[left(idx)] + self.tree[right(idx)]

    # Update element of array present at index pos with value=new_val and update Segment Tree with the new sum
    # update(index,new_value)
    def update(self, pos, new_val):
        start = self.tree_size + pos
        self.tree[start] = new_val
        start //= 2
        while start:
            self.tree[start] = self.tree[left(start)] + self.tree[right(start)]
            start //= 2

    # Return Sum of element present in [range_left,range_right] of array both inclusive
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
lst = list(read())
st = SegmentTree([0] * 2 * n)
ans = [[] for i in range(n)]
for idx, el in enumerate(lst):
    t = ans[el - 1]
    t.append(idx)
    if len(ans[el - 1]) == 2:
        x = st.range_sum(t[0], t[1])
        st.update(t[0], 1)
        ans[el - 1] = t[1] - t[0] - 1 - 2 * x
print(*ans)
