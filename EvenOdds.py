import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    count = (n + 1) // 2
    
    if k <= count:
        print(2*k - 1)
    else:
        print(2*(k - count))

main()
