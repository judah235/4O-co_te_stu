n,m=map(int,input().split())

if n==2:
    print(4 if (m-1)//2>4 else (m-1)//2+1)
elif n==1:
    print(1)
elif 4<=m<7:
    print(4)
elif m<=3:
    print(m)
else:
    print(m-7+5)
    