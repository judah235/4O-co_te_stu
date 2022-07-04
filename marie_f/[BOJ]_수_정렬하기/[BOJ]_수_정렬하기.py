n =int(input()) #5

n_array = []
for i in range(n):  #0 1 2 3 4
  n_array.append(int(input()))

dual_remove_array = set(n_array)
sort_array = sorted(dual_remove_array)

for j in sort_array:
  print(j)