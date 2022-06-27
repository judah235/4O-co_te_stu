words = input().upper()
del_duple_words = list(set(words))

li_1 = []
for i in del_duple_words:
    cmp = words.count(i)
    li_1.append(cmp)

a =li_1.count(max(li_1))

if a > 1:
    print('?')
else:
    max_index = li_1.index(max(li_1))
    print(del_duple_words[max_index])