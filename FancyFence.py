import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def main():
    t = inp()
    for _ in range(t):
        a = inp()
        if 360 %(180-a) ==0:
            print("YES")
        else:
            print("NO")

main()