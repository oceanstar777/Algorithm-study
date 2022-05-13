n,m = tuple(map(int,input().split()))
cards = list(map(int,input().split()))
sum_of_cards = []   #카드합을 저장할 리스트 
for i in range(n-2):        
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if (sum:= cards[i]+cards[j]+cards[k])<=m:   #만약 sum이 m 보다 작다면
                sum_of_cards.append(sum)        #리스트에 sum 값 추가
print(max(sum_of_cards))    #리스트에서 가장 큰 값 출력
