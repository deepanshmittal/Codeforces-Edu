# Submission Link: https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/submission/164184468


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
        self.tree = [array("b", [0] * 41) for _ in range(2 * self.tree_size)]
        for idx in range(self.size):
            self.tree[self.tree_size + idx][arr[idx]] = 1
        for idx in reversed(range(1, self.tree_size)):
            left_lst, right_lst = self.tree[left(idx)], self.tree[right(idx)]
            for i in range(41):
                self.tree[idx][i] = left_lst[i] | right_lst[i]

    # Update element of array present at index pos with value=new_val and update Segment Tree with the new sum
    # update(index,new_value)
    def update(self, pos, new_val):
        start = self.tree_size + pos
        self.tree[start] = array("b", [0] * 41)
        self.tree[start][new_val] = 1
        start = start // 2
        while start:
            left_lst, right_lst = self.tree[left(start)], self.tree[right(start)]
            for i in range(41):
                self.tree[start][i] = left_lst[i] | right_lst[i]
            start //= 2

    # Return Sum of element present in [range_left,range_right] of array both inclusive
    def query(self, range_left, range_right):
        s = array("b", [0] * 41)
        range_left += self.tree_size
        range_right += self.tree_size
        while range_left <= range_right:
            if range_left & 1:
                lst = self.tree[range_left]
                for i in range(41):
                    s[i] |= lst[i]
                range_left += 1
            if not range_right & 1:
                lst = self.tree[range_right]
                for i in range(41):
                    s[i] |= lst[i]
                range_right -= 1
            range_right //= 2
            range_left //= 2
        return s.count(1)


n, m = read()
lst = list(read())
st = SegmentTree(lst)
for x in range(m):
    q = list(read())
    if q[0] == 2:
        st.update(q[1] - 1, q[2])
    else:
        print(st.query(q[1] - 1, q[2] - 1))
