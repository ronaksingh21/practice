import sys
input = sys.stdin.readline

def insr():
    s = input()
    return(list(s[:len(s) - 1]))

def main():
    pos = insr()
    count = 1
    for i in range(1, len(pos)):
        if count >=7:
            print("YES")
            return
        if i == 1:
            count+=1
        elif pos[i] == pos[i-1]:
            count+=1
        else:
            count = 1
    print("NO")
main()