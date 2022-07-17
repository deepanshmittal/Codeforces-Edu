# Submission Link: https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/submission/164651982

# Dictionary == Hash Collision

from sys import stdin
from bisect import bisect_left as bl, bisect_right as br
from collections import defaultdict, Counter, deque


def input():
    return stdin.readline()


def read(default=int):
    return list(map(default, input().strip().split()))


def solve():
    n, m = read()
    arr = []
    a, b = read(), read()
    l, r = 0, 0
    smaller = 0
    while l < n and r < m:
        if a[l] < b[r]:
            smaller += 1
            l += 1
        else:
            arr.append(smaller)
            r += 1
    arr.extend([smaller] * (m - r))
    return arr


# t = int(input())
t = 1
for test in range(t):
    print(*solve())
