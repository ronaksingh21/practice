#day 2
import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))

def main():
    cases = inp()
    for i in range(cases):
        inpa = inlt()
        l = inpa[0]
        a = inpa[1]
        b = inpa[2]
        largest = 0
        for j in range(l*2):
            curr = (a+j*b) % l
            largest = max(curr, largest)
        print(largest)
if __name__ == "__main__":
    main()
