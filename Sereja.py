import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))

def main():
    n, m = map(int,input().split())
    a = inlt()
    seen = set()
    count = 0
    ans = [0] * (n+1)
    for i in range(n-1, -1, -1):
        if a[i] not in seen:
            seen.add(a[i])
            count+=1
        ans[i+1] = count
    for i in range(m):
        curr = inp()
        print(ans[curr])
main()