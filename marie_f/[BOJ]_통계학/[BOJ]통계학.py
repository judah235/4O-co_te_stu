import sys

def avg(a):
    ans = round(sum(a) / len(a))
    return ans

def median(a):
    ans = a[len(a) // 2]
    return ans

def range_list(a):
    ans = abs(a[0]-a[-1])
    return ans

def mode(a):
    new_dic = {}
    for i in a:
        if new_dic.get(i) is None:
            new_dic[i] = 1
        else:
            new_dic[i] += 1

    max_val = max(new_dic.values())
    max_mode_list = {}
    for key, value in new_dic.items():
        if value == max_val:
            max_mode_list[key] = value
    # print('new_dic',new_dic)
    # print('최대 사용한 애들만',max_mode_list)
    b = list(max_mode_list.keys())
    if len(b) == 1:
        c = b[0]
    else :
        c = b[1]
    return c
#------------------------------------------------------
n = int(input())
n_list = []
for i in range(n):
    n_list.append(int(input()))
l = sorted(n_list)
#print(type(l))
#-------------------------------------------------------
print(avg(l))
print(median(l))
print(mode(l))
print(range_list(l))