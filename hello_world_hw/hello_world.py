#Import array function from the array module
from array import array as uhray

#Bind a string to a name
test_string = "apple"

#Create a variable with an integer value
test_integer = "818"

#Create a list with various data types and output a specific value from it
test_list = [2.718, "book", True, 1706, ["a", "b"]]
print("4th value in Test List:" , test_list[3])

#Add a value to the end of the list and output the result
test_list.append(test_string)
print("Test List:" , test_list , "\n")

#Create an array of a specific data type and output array
test_array = uhray('i', [5, 3, 11, 19, 3, 3, 53])

#Count the occurences of a value in the array and output the result
x0 = test_array.count(3)
print("3s in Test Array:" , x0)

#Insert a value into the array + output array before and after
print("Test Array(pre-insert):" , test_array)
test_array.insert(2, -251)
print("Test Array(post-insert):" , test_array , "\n")

#Convert array to list + output
print(test_array.tolist())
x1 = test_array.pop(4)
print(x1)
print(test_array)
test_array.insert(4, x1)
print(test_array)

#Create variables
y0 = 0
y0_list = []

#Use a 'while' loop to auto-iterate a list
while y0 < 10:
    y0_list.append(y0)
    y0 = y0 + 1

print(y0_list[6])

y0_array = uhray('i', y0_list)
print(y0_array)

test_array.extend(y0_array)
print(test_array)