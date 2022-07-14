import sys
input=sys.stdin.readline

n=int(input())
n_l=[]

for _ in range(n):
    n_l.append(int(input()))

n_l=n_l[::-1]
cnt=0

while len(n_l)!=1 and len(n_l)!=0:
    min_num=min(n_l)
    ind=n_l.index(min_num)
    n_l_sub=n_l[ind:]
    for i in range(1,len(n_l_sub)):
        if n_l_sub[i]>=n_l_sub[i-1]:
            cnt+=(n_l_sub[i]-n_l_sub[i-1]+1)
            n_l_sub[i]=n_l_sub[i-1]-1
    n_l=n_l[:ind]
print(cnt)