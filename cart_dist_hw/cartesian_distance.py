# [one-argument]
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
        temp = ((pts[0] - pts[2]) ** 2) + ((pts[1] - pts[3]) ** 2)
        # use square root function from calc.py
        g = 1
        for k in range (0, 100):
            g = (g + (temp / g)) / 2

    # output distance between points
    return f"Distance between ({pts[0]},{pts[1]}) and ({pts[2]},{pts[3]}): {round(g, 5)}"

#"""
print(cdis())
print(cdis([2,2,8,6]))
print(cdis([5,-5,-6,3]))
print(cdis(1))
print(cdis([1]))
print(cdis([1,2,"tre",4]))
#"""

"""
# [two-argument]
def cdis(p1, p2):
    # only accept 'list' type args
    if (type(p1) or type(p2)) != list:
          return f"Argument types must be 'list' -> [x,y]."
    
    # collect point coordinates from arg lists
    else:
        temp = ((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2)
        g = 1
        for k in range (0, 100): # use square root function from calc.py
            g = (g + (temp / g)) / 2

    # output distance between points
    return f"Distance between ({p1[0]},{p1[1]}) and ({p2[0]},{p2[1]}): {round(g, 5)}"

print(cdis([2,2],[8,6]))
print(cdis([5,-5],[-6,3]))
print(cdis(1,2))
"""
"""
# [four-argument]
def cdis(x1, y1, x2, y2):
    tvar0 = (x1 - x2) ** 2
    tvar1 = (y1 - y2) ** 2
    tvar2 = tvar0 + tvar1
    g = 1
    for k in range (0, 100):
            g = (g + (tvar2 / g)) / 2
    return f"Distance between ({x1},{y1}) and ({x2},{y2}): {round(g, 5)}"

print(cdis(2,2,8,6))
print(cdis(5,-5,-6,3))
"""