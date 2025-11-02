#Stack functions

def add(stack, element):      # define function/args
    stack.insert(0, element)  # first arg is index, index = 0 -> head
    return stack              # output stack for confirmation

def remove(stack):
    stack.pop(0)              # remove youngest element
    return stack

def head(stack):
    return stack[0]           # output value at index = 0

def tail(stack):              # output oldest value and index
    return f"{stack[len(stack) - 1]} @ i({len(stack) - 1})"

#Function testing

omar = []         # initiate stack structure

add(omar, 2)      # add elements
add(omar, "the")
add(omar, 685)
add(omar, 476)
add(omar, 11)
add(omar, True)
print(omar)       # output: [True, 11, 476, 685, 'the', 2]

remove(omar)      # remove elements
remove(omar)
print(omar)       # output: [476, 685, 'the', 2]

                  # retrieve 'head' and 'tail' components
print(head(omar)) # output: 476
print(tail(omar)) # output: 2 @ i(3)