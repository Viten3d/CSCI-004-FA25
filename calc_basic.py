def calc(n1, op, n2):     # define function and arguments
    if op == 0:           # addition statement
        return n1 + n2
    elif op == 1:         # subtraction statement
        return n1 - n2
    elif op == 2:         # multiplication statement
        return n1 * n2
    elif op == 3:         # division statement
        return n1 / n2
    else:
        return f"Invalid operator."
    
#"""
print(f"5 + 5 = {calc(5,0,5)}")
print(f"1 + (-1) = {calc(1,0,-1)}")
print(f"0 - (-1) = {calc(0,1,-1)}")
print(f"0 ÷ 5 = {calc(0,3,5)}")
print(f"4 ÷ 2 = {calc(4,3,2)}")
print(f"2 x 1 = {calc(2,2,1)}")
print(f"3 x 2 = {calc(3,2,2)}")
print(f"op = 5 -> {calc(2,5,3)}")
#"""