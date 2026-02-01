import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def main():
    n = inp()
    laptops = []
    happy = False
    for _ in range(n):
        a, b = map(int, input().split())
        laptops.append((a, b))
    laptops.sort()

    for i in range(1,n):
        if laptops[i-1][1] > laptops[i][1]:
            happy = True
            break
    if happy == True:
        print("Happy Alex")
    else:
        print("Poor Alex")
main()