#Function 0
#Obtain a user-generated list of integers, then remove all even values from that list.


from math import remainder as rem

#user inputs integer value; convert input string to integer unsing int()
input_list_len = int(input('First choose the list length as an integer between 1 and 10 (inclusive): '))
print()

#while statement preventing values 'int < 1' and 'int > 10' from being used
while input_list_len < 1 or input_list_len > 10:
    print("Value must be between 1 and 10.")
    input_list_len = int(input('Choose the list length: '))
    print()

print("Now create a list of" , input_list_len , "integer values.\n")

#generate a list from user inputs
ivar = 0 #temp var for iterating loop
input_list = []

while ivar < input_list_len:
    input_list.append(int(input('Enter value: ')))
    ivar = ivar + 1

print("\nInitial list:" , input_list)

#search for and remove even values from the list
ivar = input_list_len - 1 #set ivar to start at final index
even_list = [] #list for removed values

while ivar > -1:
    lvar = input_list[ivar] #temp var for reducing clutter
    if rem(lvar, 2) == 0 and lvar != 0: #not considering '0' as even
        even_list.append(lvar)
        input_list.pop(ivar)
    ivar = ivar - 1

print("Altered list:" , input_list)
print("Removed values:" , even_list)

#Function 1
"""first attempt
#input s.g. measurements
igrav = float(input('Starting S.G.: '))
fgrav = float(input('Final S.G.: '))

#calculate abv using formula
abv = 131.25 * (igrav - fgrav)

print("Alcohol by volume:" , abv)
"""