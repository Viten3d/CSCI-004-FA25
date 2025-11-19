#Function 0
#Obtain a user-generated list of integers, then remove all even values from that list.

from math import remainder as rem

def clean(input_list:list):
    input_list_len = len(input_list)
    ivar = input_list_len - 1 #set iterator variable to value of final index

    #search for and remove even values from the list
    while ivar > -1:
        lvar = input_list[ivar] #temp var for reducing clutter
        if rem(lvar, 2) == 0 and lvar != 0: #not considering '0' as even
            input_list.pop(ivar)
        ivar = ivar - 1

    return input_list