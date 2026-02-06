import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
from collections import Counter
def main():
    n = int(input())
    initial = Counter(list(map(int,input().split())))
    first = Counter(list(map(int,input().split())))
    second = Counter(list(map(int,input().split())))
    # initial = Counter([1,5,8,123,7])
    # first = Counter([123,7,5,1])
    # second = Counter([5,1,7])
    # err2= [item for item in first if item not in second]
    # err1= [item for item in initial if item not in first]
    err1 = initial - first
    err2 = first - second
    err1, junk = err1.popitem()
    err2, junk = err2.popitem()
    print(err1)
    print(err2)
main()

    
    