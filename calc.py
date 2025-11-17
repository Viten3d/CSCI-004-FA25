def calc(n1=None, op=None, n2=None):             # define function and arguments
    if n1 == None and op == None and n2 == None: # if no args are given, then display operator codes + format
        return f"[1-ARG]\ncalc(<integer(n)>,<operator code>)\nAbs: 0\nFac: 1 (n > 1)\nSqt: 2 (n > 0)\nD2B: 3 (n > 0)\n\n[2-ARG]\ncalc(<integer>,<operator code>,<integer>)\nAdd: 0\nSub: 1\nMul: 2\nDiv: 3\nPow: 4\nCon: 5 (n >= 0)\nMdl: 6\n"

    # [single-argument functions]
    # if and only if the first two args are given *and* arg types are integers, then run desired operation
    elif type(n1) == int and type(op) == int and n2 == None:
        if op == 0:                 # absolute value statement
            if n1 >= 0:
                return n1
            else:
                return -n1
        elif op == 1 and n1 > 1:    # factorial statement
            for k in range(1, n1):
                n1 = n1 * k
            return n1
        elif op == 2 and n1 > 0:    # square root statement
            temp = 1
            for k in range (0, 100):
                temp = (temp + (n1 / temp)) / 2
            return temp
        elif op == 3 and n1 > 0:    # decimal to binary conversion
            # look for biggest x where 2^x <= n1
            pwr = 0
            while 2 ** pwr <= n1:
                pwr += 1
            pwr -= 1 # account for the final increment that ended loop

            # create placeholder list for the binary digits
            binlst = []
            for k in range(0, pwr): # add 'x' zeros to the list
                binlst.append(0)

            # check descending powers of 2 and update list accordingly
            psum = 2 ** pwr
            for k in range(1, pwr + 1):
                psum += (2 ** (pwr - k))
                if psum > n1:
                    psum -= (2 ** (pwr - k))
                else:
                    binlst[pwr - k] = 1

            # format the binary list values as an integer
            bin_num = "1"
            k = pwr - 1
            while k >= 0: # concatenate binary digits
                bin_num += str(binlst[k])
                k -= 1

            return int(bin_num) # return binary number
        else:
            if (n1 <= 1 and op == 1) or (n1 <= 0 and (op == 2 or op == 3)):
                return "Argument too small."
            else:
                return "Invalid operator argument."

    # [dual-argument functions]
    # if and only if all args are given *and* arg types are integers, then run desired operation
    elif type(n1) == int and type(op) == int and type(n2) == int:
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
        elif op == 5 and n1 >= 0 and n2 >= 0: # concatenation statement
            n1 = str(n1)      # convert n1 and n2 to strings
            n2 = str(n2)
            x = n1 + n2
            return int(x)     # return result as an integer for use in further calculations
        elif op == 6:         # modulo statement
            return n1 % n2
        else:
            if op == 5 and (n1 < 0 or n2 < 0):
                return "Argument(s) too small."
            else:
                return "Invalid operator argument."
    else:
        if n1 != None and op == None and n2 == None:
            return "Insufficient arguments."
        elif type(n1) != int or type(op) != int or type(n2) != int:
            return "Invalid argument type."
        else:
            return "Rare error achieved."

# testing
#"""
print("Function Info:")
print(calc())

print("Function test results:")
print(f"Abs: {calc(-40,0)}")   #    |-40| -> 40
print(f"Fac: {calc(5,1)}")     #       5! -> 120
print(f"Sqt: {calc(256,2)}")   #     √256 -> 16.0
print(f"Add: {calc(1,0,-1)}")  # 1 + (-1) -> 0
print(f"Sub: {calc(3,1,-3)}")  # 3 - (-3) -> 6
print(f"Mul: {calc(5,2,2)}")   #    5 * 2 -> 10
print(f"Div: {calc(0,3,4)}")   #    0 / 4 -> 0.0
print(f"Pow: {calc(2,4,5)}")   #   2 ** 5 -> 32
print(f"Con: {calc(7,5,9)}")   #   7 || 9 -> 79
print(f"Mdl: {calc(22,6,3)}")  #   22 % 3 -> 1
print(f"D2B: {calc(6,3)}")     #     6_10 -> 110_2

print("\nError testing:")
print(f"1: {calc(11)}")        # incorrect amount of arguments
print(f"2: {calc(False,0)}")   # incorrect argument type (1-arg)
print(f"3: {calc(0,3.0,23)}")  # incorrect argument type (2-arg)
print(f"4: {calc(6,24)}")      # operator out of range (1-arg)
print(f"5: {calc(6,24,7)}")    # operator out of range (2-arg)
print(f"6: {calc(-5,1)}")      # factorial argument too small
print(f"7: {calc(0,2)}")       # square root argument too small
print(f"8: {calc(0,5,-5)}")    # concatenation argument too small
print(f"9: {calc(-6,3)}")      # binary conversion arg too small
#"""
