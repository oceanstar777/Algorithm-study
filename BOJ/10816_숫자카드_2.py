def upper_bound(num, lst,start,end):
    while(start < end):
        mid = (start+end)//2
        if lst[mid] <= num:
            start = mid + 1
        else:
            end = mid
    return end

def lower_bound(num, lst,start,end):
    while(start < end):
        mid = (start + end) // 2
        if lst[mid] < num:
            start = mid + 1
        else:
            end = mid
    return end

n = int(input())
cards = sorted(map(int,input().split()))
m = int(input())
targets = list(map(int,input().split()))

for num in targets:
    print(upper_bound(num,cards,0,n) - lower_bound(num,cards,0,n),end = ' ')
