# This is a function for calculating distances between points on a complex plane.
# This function will take the entire coordinate as x+yi, instead of just taking x and y independently.

# Coming Soon: Support for coordinates with only one component (x, -x, yi, -yi)

# square root approximator function
def sqrt(rdc):
    if rdc == 0:
        return 0
    g = 1
    for k in range (0, 100):
        g = (g + (rdc / g)) / 2
    return g

# complex distance function
def complex_dist(coords):   # define function
    # check if coordinate only has x component
    
    # check if x-values are negative
    x1_neg = 0              # memory variables
    x2_neg = 0
    if coords[0][0] == '-': # remove negative if present so operator check isn't broken
        coords[0] = coords[0].removeprefix('-')
        x1_neg = 1
    if coords[1][0] == '-':
        coords[1] = coords[1].removeprefix('-')
        x2_neg = 1
    #"""
    # determine where the operators are
    oplst = [0,0]           # list to store operator indices
    for c in range(0, 2):   # search for operator location
        t = 0               # temporary variables
        n = 0
        while (t != '+') and (t != '-'): # check value is an operator
            t = coords[c][n]             # retrieve character from coordinate for while check
            n += 1                       # increment to check next character
        oplst[c] = n - 1                 # add operator indices to list
    
    # create variables representing operator indices
    op1 = oplst[0]
    op2 = oplst[1]

    # retrieve x and y values
    if op1 == 1:          # if the second character is the operator,
        x1 = coords[0][0] # then the first character is x
    else:                 # if not, concatenate characters up to operator
        x1 = coords[0][0]
        for k in range(1, op1):
            x1 = str(x1) + str(coords[0][k])

    if len(coords[0]) - op1 == 3: # if the difference between the length of the coordinate string and the operator index is 3,
        y1 = coords[0][op1 + 1]   # then the character after the operator is y
    else:
        y1 = coords[0][op1 + 1]
        for k in range(op1 + 2, len(coords[0]) - 1):
            y1 = str(y1) + str(coords[0][k])

    if op2 == 1:
        x2 = coords[1][0]
    else:
        x2 = coords[1][0]
        for k in range(1, op2):
            x2 = str(x2) + str(coords[1][k])

    if len(coords[1]) - op2 == 3:
        y2 = coords[1][op2 + 1]
    else:
        y2 = coords[1][op2 + 1]
        for k in range(op2 + 2, len(coords[1]) - 1):
            y2 = str(y2) + str(coords[1][k])
#"""
    # convert x and y values back to numerical values
    if x1_neg == 1:
        x1 = -float(x1)
    else:
        x1 = float(x1)
    if coords[0][op1] == '-':
        y1 = -float(y1)
    else:
        y1 = float(y1)
    if x2_neg == 1:
        x2 = -float(x2)
    else:
        x2 = float(x2)
    if coords[1][op2] == '-':
        y2 = -float(y2)
    else:
        y2 = float(y2)
    #return f"x1: {x1} | y1: {y1} | x2: {x2} | y2: {y2}" #debug
    return sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
#"""

print(complex_dist(['-25-44i','-52+233i']))