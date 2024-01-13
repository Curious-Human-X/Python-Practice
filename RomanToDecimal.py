#User Input & Capitalization
roman_num = input("\n[Use I, V, X, L, C, D, M]\nEnter the Roman Numeral: ")
roman = roman_num.upper()
roman_len = len(roman)

#List of numbers
numbers = []
converted = []

#Convertion Reference
convert = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

#Creating a list of roman numbers
for i in range(0,roman_len):
    numbers.append(roman[i])

#Converts from Roman to Numbers 
for number in numbers:
    if number in convert:
        converted.append(convert[number])
		
#Calculation For Convertion
def convertion(roman):
	decimal = 0
	index = 0
    
	#Checks all the digits
	while (index < len(converted)):

		if (index + 1 < len(converted)):

			if (converted[index] >= converted[index + 1]):
				decimal = decimal + converted[index]
				index = index + 1
				
			else:
				decimal = decimal + converted[index + 1] - converted[index]
				index = index + 2
			
		else:
			decimal = decimal + converted[index]
			index = index + 1
			
	return decimal

print(f"\nThe Decimal form of {roman} is {convertion(roman)}.\n")