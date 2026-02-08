
import sys
input = sys.stdin.readline 

def main():
    #format(number, 'b')
    n,m,k = map(int, input().split())
    friends = [int(input().strip()) for friend in range(m)]
    fedor = format(int(input()), f'0{n}b')
    count = 0
    for i in range(m):
        curr = format(friends[i],f'0{n}b')
        diff = 0
        for j in range(n):
            if curr[j]!= fedor[j]:
                diff +=1
        
        if diff <= k:
            count +=1
    print(count)
main()