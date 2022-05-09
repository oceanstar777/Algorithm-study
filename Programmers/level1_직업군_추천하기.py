def solution(table,languages,preference):
    table = [string.split() for string in table]    #table을 순회하면서 들어온 문자열을 split으로 분리하여 2차원 배열 생성
    prefer_dct =dict(zip(languages,preference))     #사용언어를 key 선호도를 value로하는 딕셔너리 생성
    score_lst= []                               #점수를 저장할 리스트 생성
    for row in table:                           #table의 행을 순회
        score = 0                               #행을 모두 순회할때 마다 0으로 초기화
        for elem in row:                        #행의 요소들을 순회
            if elem in prefer_dct:              #요소가 prefer_dct의 key에 존재하면
                score += (6-row.index(elem))*(prefer_dct[elem])     #score에 6에서 요소의 행에서의 index를 뺀 값(점수)과 선호도의 곱을 score에저장 
        score_lst.append(score)                 #점수 리스트에 점수 추가
    res = [(row[0],score) for row,score in zip(table,score_lst)]    #(직업,점수)튜플을 요소로하는 리스트 생성
    return sorted(res,key = lambda x : (-x[1],x[0]))[0][0]          #점수, 사전순정렬후 점수가 가장크고 사전순으로 가장빠른 요소 반환
    



table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", 
"CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", 
"HARDWARE C C++ PYTHON JAVA JAVASCRIPT", 
"PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", 
"GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]
print(solution(table,languages,preference))