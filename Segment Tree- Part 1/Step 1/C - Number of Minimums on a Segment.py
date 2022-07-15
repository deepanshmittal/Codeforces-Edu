# Submission Link: https://codeforces.com/edu/course/2/lesson/4/1/practice/contest/273169/submission/164071019

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
        self.tree = [[float("inf"), 1] for i in range(2 * self.tree_size)]
        for i in range(self.tree_size, self.tree_size + self.size):
            self.tree[i] = [arr[i - self.tree_size], 1]
        for idx in reversed(range(1, self.tree_size)):
            if self.tree[left(idx)][0] == self.tree[right(idx)][0]:
                self.tree[idx] = [self.tree[left(idx)][0],
                                  self.tree[left(idx)][1] + self.tree[right(idx)][1]]
            else:
                self.tree[idx] = min(self.tree[left(idx)], self.tree[right(idx)]).copy()
        self.idx, self.left_node, self.right_node = [1, 0, self.size - 1]

    # Update element of array present at index pos with value=new_val and update Segment Tree with the new sum
    # update(index,new_value)
    def update(self, pos, new_val):
        start = self.tree_size + pos
        self.tree[start] = [new_val, 1]
        start >>= 1
        while start:
            if self.tree[left(start)][0] == self.tree[right(start)][0]:
                self.tree[start] = [self.tree[left(start)][0],
                                    self.tree[left(start)][1] + self.tree[right(start)][1]]
            else:
                self.tree[start] = min(self.tree[left(start)], self.tree[right(start)]).copy()
            start >>= 1

    # Return Sum of element present in [range_left,range_right] of array both inclusive
    def range_min(self, range_left, range_right):
        range_left += self.tree_size
        range_right += self.tree_size
        MIN = [float("inf"), 1]
        while range_left <= range_right:
            if range_left & 1:
                if MIN[0] == self.tree[range_left][0]:
                    MIN[1] += self.tree[range_left][1]
                else:
                    MIN = min(MIN, self.tree[range_left]).copy()
                range_left += 1
            if not range_right & 1:
                if MIN[0] == self.tree[range_right][0]:
                    MIN[1] += self.tree[range_right][1]
                else:
                    MIN = min(MIN, self.tree[range_right]).copy()
                range_right -= 1
            range_right >>= 1
            range_left >>= 1
        return MIN


n, m = read()
lst = list(read())
st = SegmentTree(lst)
# print(st.tree)
for x in range(m):
    q = list(read())
    if q[0] == 1:
        st.update(q[1], q[2])
    else:
        print(*st.range_min(q[1], q[2] - 1))