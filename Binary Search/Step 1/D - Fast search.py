# Submission Link: https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/submission/163139481

from sys import stdin
from bisect import bisect_left as bl, bisect_right as br
from collections import defaultdict, Counter, deque

input = stdin.readline


def read(default=int):
    return list(map(default, input().strip().split()))


def solve():
    n = read()[0]
    lst, k = sorted(read()), read()[0]
    for i in range(k):
        l, r = read()
        print(br(lst, r) - bl(lst, l), end=" ")


# t = int(input())
t = 1
for test in range(t):
    solve()
