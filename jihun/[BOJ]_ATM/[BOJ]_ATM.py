input()

P_l=list(map(int,input().split()))
P_l.sort()
ans=0
for i in range(1,len(P_l)+1):
    ans+=sum(P_l[:i])
print(ans)