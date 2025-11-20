# square root function from calc.py
def sqrt(temp):
    if temp == 0: # protect from g converging to 0
        return 0
    g = 1
    for k in range (0, 100):
        g = (g + (temp / g)) / 2
    return g

# cartesian distance function
def cdis(cds=None):
    # print usage info when ran with no argument
    if cds == None:
        return f"Argument: cdis([<x1>,<y1>,<x2>,<y2>]) 0R cdis([<x1>,<y1>,<z1>,<x2>,<y2>,<z2>])\nTypes: list with integer and/or float elements\n"

    # only accept a 'list' type arg
    elif type(cds) != list:
        return f"Argument type must be 'list'. Help: cdis()"

    # only accept a list with four or six values
    elif (len(cds) != 4) and (len(cds) != 6):
        return f"List must have four or six numbers. Help: cdis()"
    
    # only accept a list with values of type integer or float, then return distance (4-coord)
    elif len(cds) == 4:
        if (type(cds[0]) != int and type(cds[0]) != float) or (type(cds[1]) != int and type(cds[1]) != float) or (type(cds[2]) != int and type(cds[2]) != float) or (type(cds[3]) != int and type(cds[3]) != float):
            return f"List values must be of type 'int' or 'float'. Help: cdis()"
        else: # plug values from list into 2D distance formula
            return sqrt(((cds[0] - cds[2]) ** 2) + ((cds[1] - cds[3]) ** 2))
    
    # only accept a list with values of type integer or float, then return distance (6-coord)
    elif len(cds) == 6:
        if (type(cds[0]) != int and type(cds[0]) != float) or (type(cds[1]) != int and type(cds[1]) != float) or (type(cds[2]) != int and type(cds[2]) != float) or (type(cds[3]) != int and type(cds[3]) != float) or (type(cds[4]) != int and type(cds[4]) != float) or (type(cds[5]) != int and type(cds[5]) != float):
            return f"List values must be of type 'int' or 'float'. Help: cdis()"
        else: # plug values from list into 3D distance formula
            return sqrt(((cds[0] - cds[3]) ** 2) + ((cds[1] - cds[4]) ** 2) + ((cds[2] - cds[5]) ** 2))

#"""
print(f"Info:\n{cdis()}")
print(f"D[(2,2),(8,6)] = {round(cdis([2,2,8,6]),5)}")
print(f"D[(5,-5),(-6,3)] = {round(cdis([5,-5,-6,3]),5)}")
print(f"D[(-6,3),(5,-5)] = {round(cdis([-6,3,5,-5]),5)}")
print(f"D[(4,4,4),(0,0,0)] = {round(cdis([4,4,4,0,0,0]),5)}")
print(f"D[(-6,3,1),(9,-2,7)] = {round(cdis([-6,3,1,9,-2,7]),5)}")
print(f"D[(9,-2,7),(-6,3,1)] = {round(cdis([9,-2,7,-6,3,1]),5)}")
print(f"Wrong arg type -> {cdis(1)}")
print(f"Not enough values -> {cdis([1])}")
print(f"Non-numerical arg (4) -> {cdis([1,2,"tre",4])}")
print(f"Non-numerical arg (6) -> {cdis([1,True,3,4,[5],6])}")
#"""