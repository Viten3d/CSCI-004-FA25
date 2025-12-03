# square root function from calc.py (for distance formulas)
def sqrt(temp):
    if temp == 0: # protect from g converging to 0
        return 0
    g = 1
    for k in range (0, 100):
        g = (g + (temp / g)) / 2
    return g

# euclidean distance function
def edist(cds=None):
    # print usage info when ran with no argument
    if cds == None:
        return f"Argument Syntax:\nedist([<x1>,<x2>])\nedist([<x1>,<y1>,<x2>,<y2>])\nedist([<x1>,<y1>,<z1>,<x2>,<y2>,<z2>])\nTypes: 'list' with 'int' and/or 'float' elements\n"

    # only accept a 'list' type arg
    elif type(cds) != list:
        return f"Argument type must be 'list'. Help: edist()"

    # only accept a list with two, four, or six values
    elif (len(cds) != 2) and (len(cds) != 4) and (len(cds) != 6):
        return f"List must have two, four, or six numbers. Help: edist()"
    
    # only accept a list with values of type integer or float, then return distance (1D)
    elif len(cds) == 2:
        if (type(cds[0]) != int and type(cds[0]) != float) or (type(cds[1]) != int and type(cds[1]) != float):
            return f"List values must be of type 'int' or 'float'. Help: edist()"
        else: # plug values from list into 1D distance formula
            return abs(cds[0] - cds[1])

    # only accept a list with values of type integer or float, then return distance (2D)
    elif len(cds) == 4:
        if (type(cds[0]) != int and type(cds[0]) != float) or (type(cds[1]) != int and type(cds[1]) != float) or (type(cds[2]) != int and type(cds[2]) != float) or (type(cds[3]) != int and type(cds[3]) != float):
            return f"List values must be of type 'int' or 'float'. Help: edist()"
        else: # plug values from list into 2D distance formula
            return sqrt(((cds[0] - cds[2]) ** 2) + ((cds[1] - cds[3]) ** 2))
    
    # only accept a list with values of type integer or float, then return distance (3D)
    elif len(cds) == 6:
        if (type(cds[0]) != int and type(cds[0]) != float) or (type(cds[1]) != int and type(cds[1]) != float) or (type(cds[2]) != int and type(cds[2]) != float) or (type(cds[3]) != int and type(cds[3]) != float) or (type(cds[4]) != int and type(cds[4]) != float) or (type(cds[5]) != int and type(cds[5]) != float):
            return f"List values must be of type 'int' or 'float'. Help: edist()"
        else: # plug values from list into 3D distance formula
            return sqrt(((cds[0] - cds[3]) ** 2) + ((cds[1] - cds[4]) ** 2) + ((cds[2] - cds[5]) ** 2))

#"""
print(f"Info:\n{edist()}")
print(f"D[-5,3] = {edist([-5,3])}")
print(f"D[(5,-5),(-6,3)] = {round(edist([5,-5,-6,3]),5)}")
print(f"D[(-6,3,1),(9,-2,7)] = {round(edist([-6,3,1,9,-2,7]),5)}")
print(f"Wrong arg type -> {edist(1)}")
print(f"Not enough values -> {edist([1])}")
print(f"Non-numerical arg (1D) -> {edist([False, 67])}")
print(f"Non-numerical arg (2D) -> {edist([1,2,"tre",4])}")
print(f"Non-numerical arg (3D) -> {edist([1,True,3,4,[5],6])}")
#"""