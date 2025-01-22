import sys
from sys import setrecursionlimit

setrecursionlimit(10000)

def f(n):
    if n >= 2025:
        return 1
    if n < 2025:
        print(n)
        return n - f(n + 2) - f(n + 4)

print(f(20) + f(25))