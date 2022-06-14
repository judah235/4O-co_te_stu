## 더하기 사이클

[문제 링크](https://www.acmicpc.net/problem/1110)

N_st로 인풋을 받고

if 들어온 숫자의 크기가 1자리 수 (0~9)인 경우
 -> 0+(1자리 수)

else 2자리 이상 수(10~99)
 -> 그대로

while문에서 맨 처음 입력 N_st 숫자와 while문을 돌며 마지막 출력 숫자가 같아지면
while문을 탈출하고
몇 번 반복하였는지 circle변수로 count함.