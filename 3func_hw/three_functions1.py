#Function 1
#Calculate alcohol content (abv) using specific gravity readings as inputs

#define function
def abvcalc(igrav=0, fgrav=0):
    abv = 131.25 * (igrav - fgrav)
    return round(abv, 2) #round value to avoid (looking at) float imprecision

#output called function
#print("ABV: " , abvcalc(1.09, 1.01) , "%", sep='')