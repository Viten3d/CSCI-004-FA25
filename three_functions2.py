#test using function1 in another namespace
from three_functions1 import abvcalc as abv
print("ABV: " , abv(1.09, 1.01) , "%", sep='')

#Function 2
#Use the Newton-Raphson method to approximate the square root of a given number using a guess (number > 0, guess > 0)

def sqrtapx(rdcn, guess):
    ivar = 0
    ansr = (guess + (rdcn / guess)) * (1 / 2)
    while ivar < 50:
        ansr = (ansr + (rdcn / ansr)) * (1 / 2)
        ivar = ivar + 1
    return ansr

#test output
print(sqrtapx(2, 0.01))