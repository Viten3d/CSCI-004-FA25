# [two-argument]
def cdis(p1, p2):
    # only accept exactly two args
    if (p1 or p2) == None:
          return f"Insufficient arguments."
    # only accept 'list' type args
    if (type(p1) or type(p2)) != list:
          return f"Argument types must be 'list' -> [x,y]."
    # collect point coordinates from arg lists
    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    y2 = p2[1]
    temp = ((x1 - x2) ** 2) + ((y1 - y2) ** 2)
    # use square root function from calc.py
    g = 1
    for k in range (0, 100):
            g = (g + (temp / g)) / 2
    # output distance between points
    return f"Distance between ({x1},{y1}) and ({x2},{y2}): {round(g, 5)}"

print(cdis([2,2],[8,6]))
print(cdis([5,-5],[-6,3]))
print(cdis(1,2))

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