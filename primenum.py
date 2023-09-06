numberList = [10, 501, 22, 37, 100, 999, 87, 351]

ansList = []

for num in numberList:

    if num == 0 or num == 1:  # prime num cannot be 0 and 1
        continue

    for i in range(2,
                   num // 2 + 1):  # If number is divisible by any number (i) from range then it is not prime number - (range from 2 to half of the num)
        if num % i == 0:
            break
    # If not divisible then it's a prime number so below else will be executed
    else:

        ansList.append(num)  # append prime num list

if len(ansList) != 0:  # If list is non-empty or not = 0 then print the elements

    print("Prime number List : ", ansList)
    print("Count of Prime numbers : ", len(ansList))

else:
    print("No prime numbers from the list")
