import sys
input = sys.stdin.readline

def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        minso = [0] * n
        submin = [0] * n
        for i in range(n):
            l = int(input())
            arr = list(map(int, input().split()))
            arr.sort()
            minso[i] = arr[0]
            submin[i] = arr[1]

        subsum = sum(submin)
        junk = min(submin)
        supamin = min(minso)
        if n==1:
            print(supamin)
            continue
        print(subsum - junk + supamin)
main()
        
