import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))

def main():
    coins = inp()
    values = inlt()
    values.sort(reverse = True)
    total = sum(values)
    count = 0
    curr = 0
    for i in values:
        curr+=i
        count+=1
        if curr > total//2:
            break
    print(count)
main()