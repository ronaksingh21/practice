import sys
input = sys.stdin.readline

def main():
    w = int(input())
    if w >= 4 and w % 2 == 0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()

