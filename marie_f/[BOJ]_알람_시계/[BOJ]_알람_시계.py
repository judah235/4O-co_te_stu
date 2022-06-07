h, m =  map(int, input().split())
if h == 0:
    h = 24
alarm = ((h*60)+m) - 45
h = int(alarm/60)
m = int(alarm%60)
if h == 24 :
    h = 0
print(h, m)