# Submission Link: https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/submission/164682448

# Dictionary == Hash Collision

from sys import stdin
from bisect import bisect_left as bl, bisect_right as br
from collections import defaultdict, Counter, deque


def input():
    return stdin.readline()


def read(default=int):
    return list(map(default, input().strip().split()))


def solve():
    n, s = read()
    lst = read()
    l, r = 0, 0
    x = 0
    ans = 0
    while l < n and r < n:
        while r < n and x + lst[r] <= s:
            x += lst[r]
            r += 1
        ans = max(ans, r - l)
        x -= lst[l]
        l += 1
    return ans


# t = int(input())
t = 1
for test in range(t):
    print(solve())
