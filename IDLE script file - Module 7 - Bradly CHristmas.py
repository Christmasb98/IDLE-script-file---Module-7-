evenNumbers = [ ]
oddNumbers = [ ]

for number in range (1,16):
    if number % 2 == 0:
        evenNumbers.append(number)
    else:
        oddNumbers.append(number)


print ("the even numbers are: ", evenNumbers)

print ("the odd numbers are: ", oddNumbers)
