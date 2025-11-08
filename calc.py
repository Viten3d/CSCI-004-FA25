def calc(n1=None, n2=None, op=None):               # define function and arguments
    if n1 == None and n2 == None and op == None:   # if no args given, display operator codes
        return f"Add: 0\nSub: 1\nMul: 2\nDiv: 3"

    # (only) if all args are given and arg types are integers, run desired operation
    elif type(n1) == int and type(n2) == int and type(op) == int:
        if op == 0:
            return n1 + n2                         # addition statement
        elif op == 1:
            return n1 - n2                         # subtraction statement
        elif op == 2:
            return n1 * n2                         # multiplication statement
        elif op == 3:
            return n1 / n2                         # division statement
        else:
            return "Invalid operator argument."
    else:
        return "Insufficient/invalid arguments."

# testing

print(calc())          # output codes
print(calc(1,2))       # output arg error, reason: arg(s) missing
print(calc(1.1,2.2,0)) # output arg error, reason: arg(s) not 'int'
print(calc(1,2,5))     # output operator arg error
print(calc(5,5,0))     # 5 + 5 = 10
print(calc(1,-1,0))    # 1 + (-1) = 0
print(calc(0,-1,1))    # 0 - (-1) = 1
print(calc(0,5,3))     # 0 / 5 = 0
print(calc(4,2,3))     # 4 / 2 = 2.0
print(calc(2,1,2))     # 2 * 1 = 2
print(calc(3,2,2))     # 3 * 2 = 6
