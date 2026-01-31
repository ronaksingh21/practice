import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    t = int(next(it))
    for i in range(t):
        s = ""
        n = int(next(it))
        a = [next(it) for i in range(n)]
        for j in range(n):
            after = a[j]+s
            before = s+a[j]
            if after < before:
                s = after
            else:
                s = before
        print(s)
main()
    