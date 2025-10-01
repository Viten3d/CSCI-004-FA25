from three_functions0 import clean
from three_functions1 import abvcalc as abv
from three_functions2 import sqrtapx as sqrt

#test function0
test_list = [0, 1, -2, 67, 84, 46, 903]
print("Cleaned list:" , clean(test_list))

#test function1
print("ABV: " , abv(1.09, 1.01) , "%", sep='')

#test function2
print("Square root of 64:" , sqrt(64, 10))