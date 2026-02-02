import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def main():
    test = input().strip()
    m = inp()
    # for _ in range(m):
    #     count = 0
    #     l, r = map(int, input().split())
    #     for i in range(l-1,r-1):
    #         if test[i] == test[i+1]:
    #             count +=1
    #     print(count)
    pref = [0] *len(test)
    for i in range(1,len(test)):
        pref[i] = pref[i-1]
        if test[i] == test[i-1]:
            pref[i]+=1
    
    for i in range(m):
        l,r = map(int, input().split())
        print(pref[r-1]-pref[l-1])
main()