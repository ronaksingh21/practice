import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        s= input().strip()
        cnt = [0,0]
        for i in range(len(s)):
            cnt[int(s[i])]+=1
        for i in range(len(s)+1):
            if i == len(s) or cnt[1 - int(s[i])] == 0:
                print(len(s)-i)
                break
            cnt[1-int(s[i])]-=1
main()