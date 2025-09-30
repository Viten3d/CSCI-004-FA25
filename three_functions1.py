#Function 1
#Calculate alcohol content (abv) using specific gravity readings as inputs

#define function
def abvcalc(igrav, fgrav):
    abv = 131.25 * (igrav - fgrav)
    return round(abv, 2) #round value to avoid (looking at) float imprecision

#output called function
print("ABV: " , abvcalc(1.09, 1.01) , "%", sep='')




"""first attempt
#input s.g. measurements
igrav = float(input('Starting S.G.: '))
fgrav = float(input('Final S.G.: '))

#calculate abv using formula
abv = 131.25 * (igrav - fgrav)

print("Alcohol by volume:" , abv)
"""