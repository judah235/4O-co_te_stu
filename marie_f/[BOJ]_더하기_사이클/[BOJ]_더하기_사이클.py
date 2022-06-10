N_st = input()
circle = 0
if len(N_st) < 2:
  N = str(0)+N_st
  
else: 
  N = N_st
while True: 
  circle += 1
  n1 = N[0] #0
  n2 = N[-1] # 1
  N2 = int(n1)+int(n2) #1
  N2 = str(N2)
  new_N = n2 + N2[-1] #11
  N = new_N
  if N[1] == N_st:
    break 

print(circle)