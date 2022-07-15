# Submission Link: https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/submission/164177267

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
            self.tree[idx] = max(self.tree[left(idx)], self.tree[right(idx)])

    # Update element of array present at index pos with value=new_val and update Segment Tree with the new sum
    # update(index,new_value)
    def update(self, pos, new_val):
        start = self.tree_size + pos
        self.tree[start] = new_val
        start = start // 2
        while start:
            self.tree[start] = max(self.tree[left(start)], self.tree[right(start)])
            start //= 2

    # Return Sum of element present in [range_left,range_right] of array both inclusive
    def query(self, val, pos):
        idx = self.tree_size + pos
        trace = [idx]
        idx >>= 1
        while idx and idx < self.tree_size:
            if self.tree[idx] >= val:
                if left(idx) >= trace[-1] and self.tree[left(idx)] >= val:
                    trace.pop()
                    idx = left(idx)
                elif right(idx) >= trace[-1] and self.tree[right(idx)] >= val:
                    trace.pop()
                    idx = right(idx)
                else:
                    if idx + 1 >= 2 ** idx.bit_length():
                        return -1
                    idx += 1
            else:
                trace.append(idx)
                idx >>= 1
        # print(trace)
        if idx and pos <= idx - self.tree_size < self.size:
            return idx - self.tree_size
        return -1


n, m = read()
lst = list(read())
st = SegmentTree(lst)
for x in range(m):
    q = list(read())
    if q[0] == 1:
        st.update(q[1], q[2])
    else:
        print(st.query(q[1], q[2]))
