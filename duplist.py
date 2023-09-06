
data = [[1, 2, 3, 66], [3, 4, 5], [5, 6, 7, 66]]

res = set()  #to take unique elements used set()

for i in data:
    for j in data:
        if i is not j:
            res |= set(i) & set(j)   #used "|=" union OR, will get added to res itself

print(res)

