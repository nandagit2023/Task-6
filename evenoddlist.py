
giv_list = [10, 501, 22, 37, 100, 999, 87, 351]
even_lst = []
odd_lst = []

for i in giv_list:
    if i % 2 == 0:
       even_lst.append(i)
    else:
       odd_lst.append(i)

print("Even list : ", even_lst)
print("Odd list : ", odd_lst)