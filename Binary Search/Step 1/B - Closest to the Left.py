# Submission Link: https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/submission/163138866

from sys import stdin
from bisect import bisect_left as bl, bisect_right as br
from collections import defaultdict, Counter, deque

input = stdin.readline


def read(default=int):
    return list(map(default, input().strip().split()))


def solve():
    n, q = read()
    lst, query = read(), read()
    for i in query:
        print(br(lst, i))


# t = int(input())
t = 1
for test in range(t):
    solve()
