# Submission Link: https://codeforces.com/edu/course/2/lesson/6/2/practice/contest/283932/submission/163211096

from sys import stdin
from bisect import bisect_left as bl, bisect_right as br
from collections import defaultdict, Counter, deque

input = stdin.readline


def read(default=int):
    return list(map(default, input().strip().split()))


def check(arr, l):
    x = 0
    for i in arr:
        x += i // l
    return x


def solve():
    n, k = read()
    lst = [read()[0] for i in range(n)]
    lo, hi = 0, max(lst)
    ans = 0
    while hi - lo > 10 ** -6:
        mid = lo + (hi - lo) / 2
        x = check(lst, mid)
        if x >= k:
            lo = mid
            ans = max(ans, mid)
        else:
            hi = mid
        # print(lo, hi, x)
    print(ans)


# t = int(input())
t = 1
for test in range(t):
    solve()
