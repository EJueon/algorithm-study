import sys
from collections import Counter
input = sys.stdin.readline

arr = input().strip().split(' ')
if '' in arr:
    arr.remove('')
print(len(arr))