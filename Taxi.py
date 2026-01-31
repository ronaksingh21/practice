import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def main():
    
    ngroups = inp()
    groups = inlt()
    count = 0
    c4 = groups.count(4)
    c3 = groups.count(3)
    c2 = groups.count(2)
    c1 = groups.count(1)
    
    count += c4
    count += c3
    remove = min(c3, c1)
    c1-=remove
    
    count += c2//2
    c2 = c2%2
    
    if c2 ==1:
        count+=1
        c1-=2
        if c1<0:
            c1 = 0
    count += (c1+3)//4
    
    print(count)
    # groups.sort(reverse = True)
    # for i in range(len(groups)):
    #     if groups[i] == 4:
    #         count+=1
    #     elif groups[i] == 3:
    #         for j in range(i, len(groups)):
    #             if groups[j] == 1:
    #                 groups[j]=0
    #                 groups[j]=0
    #                 count+=1
    #                 break
    #         else: 
    #             count+=1
    #             groups[i]=0
    #     elif groups[i] == 2:
    #         for j in range(i, len(groups)):
    #             if groups[j] == 2:
    #                 groups[j]=0
    #                 groups[j]=0
    #                 count+=1
    #                 break
    #             elif groups[j] == 1:
    #                 groups[i]=0
    #                 groups[j]=0
    #                 count+=1
    #                 break
    #         else: 
    #             count+=1
    #             groups[i]=0
    #     elif groups[i]==1:
    #         count +=1
    #     if groups[i] ==0:
    #         continue
    # print(count)
main()