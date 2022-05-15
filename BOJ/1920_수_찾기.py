def binary(elem,lst,start,end):
    if start > end:
        return 0
    mid = (start+end)//2
    if elem == lst[mid]:
        return 1
    elif elem < lst[mid]:
        return binary(elem, lst, start, mid-1)
    else:
        return binary(elem, lst, mid+1, end)

n = int(input())
lst = sorted(map(int,input().split()))
m = int(input())
targets = list(map(int,input().split()))

for elem in targets:
    start = 0
    end = n-1
    print(binary(elem,lst,start,end))
