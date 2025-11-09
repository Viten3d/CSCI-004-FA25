def calc(n1=None, n2=None, op=None):             # define function and arguments
    if n1 == None and n2 == None and op == None: # if no args are given, then display operator codes + format
        return f"calc(<integer>,<integer>,<operator code>)\nAdd: 0\nSub: 1\nMul: 2\nDiv: 3\nPow: 4\nCon: 5"

    # if and only if all args are given *and* arg types are integers, then run desired operation
    elif type(n1) == int and type(n2) == int and type(op) == int:
        if op == 0:           # addition statement
            return n1 + n2
        elif op == 1:         # subtraction statement
            return n1 - n2
        elif op == 2:         # multiplication statement
            return n1 * n2
        elif op == 3:         # division statement
            return n1 / n2
        elif op == 4:         # power statement
            return n1 ** n2
        elif op == 5:         # concatenation statement
            n1 = str(n1)      # convert n1 and n2 to strings
            n2 = str(n2)
            x = n1 + n2
            return int(x)     # return result as an integer for use in further calculations (see line 41)
        else:
            return "Invalid operator argument."
    else:
        return "Insufficient/invalid arguments."

# testing
#"""
print(calc())               # output codes
print(calc(1,2))            # output arg error, reason: arg(s) missing
print(calc(1.1,2.2,0))      # output arg error, reason: arg(s) not 'int'
print(calc(1,2,11))         # output operator arg error
print(calc(5,5,0))          #      5 + 5 -> 10
print(calc(1,-1,0))         #   1 + (-1) -> 0
print(calc(0,-1,1))         #   0 - (-1) -> 1
print(calc(0,5,3))          #      0 / 5 -> 0.0
print(calc(4,2,3))          #      4 / 2 -> 2.0
print(calc(2,1,2))          #      2 * 1 -> 2
print(calc(3,2,2))          #      3 * 2 -> 6
print(calc(3,2,4))          #      3 ^ 2 -> 9
print(calc(2,5,5) - 5)      # (2||5) - 5 -> 20
#"""
