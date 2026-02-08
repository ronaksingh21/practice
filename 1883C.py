import sys
input = sys.stdin.readline
import math
def main():
    t= int(input())
    for _ in range(t):
        a,k = map(int, input().split())
        cases = sorted(list(map(int,input().split())))
        least = ((cases[0]+k-1)//k)*k - cases[0]
        evens = 0
        if cases[0]%2 ==0:
            evens +=1
        for i in range(1,len(cases)):
            least = min(least, ((cases[i]+k-1)//k)*k - cases[i])
            if cases[i]%2 ==0:
                evens += 1
        if k==4:
            need = max(0,2-evens)
            least = min(least, need)
                
        print(least)
main()
                