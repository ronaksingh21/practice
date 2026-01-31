import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
# def main():
#     fence, width = inlt()
#     heights = inlt()
#     smallest = 99999999
#     idx=0
#     for i in range(len(heights) - width + 1):
#         curr = 0
#         for j in range(i, width+i):
#             curr += heights[j]
#         if curr < smallest:
#             smallest = curr
#             idx = i
#     print(idx+1)
def main():
    fence, width = inlt()
    heights = inlt()
    smallest = 0
    idx=0
    for i in range(0,width):
        smallest+= heights[i]
    curr = smallest
    for i in range(width, len(heights)):
        curr += heights[i]
        curr -= heights[i-width]
        if curr<smallest:
            idx = i - width+1
            smallest = curr
    print(idx+1)
main()
