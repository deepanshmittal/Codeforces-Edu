# Submission Link: https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/submission/164652632

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
    a, b = read(), read()
    l, r = 0, 0
    ans = 0
    while l < n and r < m:
        if a[l] == b[r]:
            val = a[l]
            x, y = 0, 0
            while l < n and a[l] == val:
                x += 1
                l += 1
            while r < m and b[r] == val:
                y += 1
                r += 1
            ans += x * y
        elif a[l] < b[r]:
            l += 1
        else:
            r += 1
    return ans


# t = int(input())
t = 1
for test in range(t):
    print(solve())
