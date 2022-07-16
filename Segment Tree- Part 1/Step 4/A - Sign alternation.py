# Submission Link: https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/submission/164426445

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
        self.tree = [[0, 0] for _ in range(2 * self.tree_size)]
        for idx in range(self.size):
            if not idx % 2:
                self.tree[self.tree_size + idx] = [arr[idx], 0]
            else:
                self.tree[self.tree_size + idx] = [0, -arr[idx]]
        for idx in reversed(range(1, self.tree_size)):
            self.tree[idx][0] = self.tree[left(idx)][0] + self.tree[right(idx)][0]
            self.tree[idx][1] = self.tree[left(idx)][1] + self.tree[right(idx)][1]

    # Update element of array present at index pos with value=new_val and update Segment Tree with the new sum
    # update(index,new_value)
    def update(self, pos, new_val):
        start = self.tree_size + pos
        if start % 2:
            self.tree[start] = [0, -new_val]
        else:
            self.tree[start] = [new_val, 0]
        start //= 2
        while start:
            self.tree[start][0] = self.tree[left(start)][0] + self.tree[right(start)][0]
            self.tree[start][1] = self.tree[left(start)][1] + self.tree[right(start)][1]
            start //= 2

    # Return Sum of element present in [range_left,range_right] of array both inclusive
    def range_sum(self, range_left, range_right):
        sum = [0, 0]
        range_left += self.tree_size
        range_right += self.tree_size
        while range_left <= range_right:
            if range_left & 1:
                sum[0] += self.tree[range_left][0]
                sum[1] += self.tree[range_left][1]
                range_left += 1
            if not range_right & 1:
                sum[0] += self.tree[range_right][0]
                sum[1] += self.tree[range_right][1]
                range_right -= 1
            range_right //= 2
            range_left //= 2
        return sum[0] + sum[1]


n = int(input().strip())
lst = list(read())
st = SegmentTree(lst)
for m in range(int(input().strip())):
    q = list(read())
    if q[0] == 0:
        st.update(q[1] - 1, q[2])
    else:
        print((-1) ** (q[1] - 1) * st.range_sum(q[1] - 1, q[2] - 1))
