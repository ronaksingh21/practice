import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):

        n,p = map(int, input().split())
        
        ls1 = list(map(int,input().split()))
        ls2 = list(map(int,input().split()))
        if n == 1:
            print(p)
            continue
        pops = list(zip(ls2,ls1))
        pops.sort()

        total = p
        notified = 1
        chiefCost = n*p
        found = False
        rem = n- notified
        for i in range(len(pops)):
            if pops[i][0] >= p:
                break
            rem = n- notified
            # if pops[i][1] == 1:
            #     continue
            if pops[i][1] >= rem:
                total += pops[i][0] * rem
                notified += rem
                rem = 0
                print(min(total, chiefCost))
                found = True
                break
            else:
                notified += pops[i][1]
                total += pops[i][1] * pops[i][0]
                rem = n- notified
        if rem >0:
            total += p*rem
        if found != True:
            print(min(total, chiefCost))
main()