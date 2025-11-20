# square root function from calc.py (used in line 30)
def sqrt(temp):
    if temp == 0: # protect from "0 problem"
        return 0
    g = 1
    for k in range (0, 100):
        g = (g + (temp / g)) / 2
    return g

# cartesian distance function
def cdis(pts=None):
    # print usage info when ran with no argument
    if pts == None:
        return f"Argument: cdis(<[x1,y1,x2,y2]>)\nTypes: list with integer and/or float elements\n"

    # only accept a 'list' type arg
    elif type(pts) != list:
        return f"Argument type must be 'list' -> [x1,y1,x2,y2]"

    # only accept a list with four values
    elif len(pts) != 4:
        return f"List must have four numbers -> [x1,y1,x2,y2]"
    
    # only accept a list with values of type integer or float
    elif (type(pts[0]) != int and type(pts[0]) != float) or (type(pts[1]) != int and type(pts[1]) != float) or (type(pts[2]) != int and type(pts[2]) != float) or (type(pts[3]) != int and type(pts[3]) != float):
        return f"List must have four numbers (type: int/float) -> [x1,y1,x2,y2]."
    
    # plug values from list into distance formula
    else:
        dist = sqrt(((pts[0] - pts[2]) ** 2) + ((pts[1] - pts[3]) ** 2))
        return dist

#"""
print(f"Info:\n{cdis()}")
print(f"D[(2,2),(8,6)] = {round(cdis([2,2,8,6]),5)}")
print(f"D[(5,-5),(-6,3)] = {round(cdis([5,-5,-6,3]),5)}")
print(cdis(1))
print(cdis([1]))
print(cdis([1,2,"tre",4]))
#"""