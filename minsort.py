


number = int(input("Enter total number of list elements : "))   #fixing total no of elements in list
L = []
for i in range (number):
    L.append(int(input("Enter each elements in list : ")))    #Having range as total of elements we can get input from user and append to empty list
print("List : ", L)

L.sort()  #Sorting to find least value in the list
print("Smallest element of the list is: ", L[0])
