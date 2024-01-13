#User Input & Capitalization
roman_num = input("Enter the Roman Numeral:\n [Use i, v, x, l, c, d, m]\n")
roman = roman_num.upper()
roman_len = len(roman)

#List of numbers
numbers = []
converted = []

#Convertion Reference
convert = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}


#Creating a list of roman numbers
for index in range(0,roman_len):
    numbers.append(roman[index])

#Converts from Roman to Numbers 
for number in numbers:
    if number in convert:
        converted.append(convert[number])

index = 0
decimal = 0
while (index < roman_len):
    if roman_len == 1:
        decimal = decimal + converted[index]
        print(decimal)
        break
    elif converted[index] >= converted[index+1]:
        decimal = decimal + converted[index] + converted[index+1]
        print(decimal)
        break
    elif converted[index] <= converted[index+1]:
        decimal = decimal + converted[index+1] - converted[index]
        print(decimal)
        break
    else:
        print(decimal)
   