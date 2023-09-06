
number = input("Enter an integer : ")

# type casting to string
number = str(number)

# store first and last digit in the number
first_digit = int(number[0])
last_digit = int(number[-1])

# Adding these two variables
addition = first_digit + last_digit

print('Addition of first and last digit of the number is : ', addition)