## 통계학

[문제 링크](https://www.acmicpc.net/problem/2108)

최빈값을 구하는 식은 딕셔너리를 이용하였음

입력이 새로만든 딕셔너리에 없으면 1을 주고(등록)
등록되어 있으면 +1해줌
-어떤 값이 가장 많이 사용했는지 

가장 많이 사용된 값을 구함
빈 딕셔너리 생성

for문으로 key, value를 갯수 샌 딕셔너리에서 가져옴 
    만약 value값이 최대면(가장 많이 사용)
        max value의 key를 저장함

b라는 변수에 list로 key값 불러옴
만약 최빈값이 한 개면 = 맨처음꺼 출력하고

최빈값이 2개 이상이면 두번째 값을 출력함



