n = int(input())
person_lst = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

for i in range(n):  
    rank = 1        #등수 1부터 시작
    for j in range(n):      
        if( person_lst[i][0] < person_lst[j][0] and 
        (person_lst[i][1] < person_lst[j][1]) ):        #몸무게와 키를 비교하여 더 가볍고 작으면
            rank+=1     #등수 증가
    print(rank,end = ' ')