import sys
input = sys.stdin.readline
from bisect import bisect_right

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))

def main():
    n = inp()
    prices = inlt()
    prices.sort()
    days = inp()
    total = []
    for i in range(days):
        budget = inp()
        total.append(bisect_right(prices, budget))
    print('\n'.join(str(item) for item in total))


    # for i in range(days):
    #     budget = inp()
    #     count = sum(num <= budget for num in prices)
    #     print(count)
main()