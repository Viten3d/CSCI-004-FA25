#Import array module
import array

#Bind a string to a name
test_string = "apple"

#Create a variable with an integer value
test_integer = "818"

#Create a list with various data types and output a specific value from it
test_list = [2.718, "book", True, 1706]
print("4th value in Test List:" , test_list[3])

#Add a value to the end of the list and output the result
test_list.append(test_string)
print("Test List:" , test_list , "\n")

#Create an array of a specific data type and output array
test_array = array.array('i', [5, 3, 11, 19, 3, 3, 53])

#Count the occurences of a value in the array and output the result
x0 = test_array.count(3)
print("3s in Test Array:" , x0)

#Insert a value into the array + output array before and after
print("Test Array(pre-insert):" , test_array)
test_array.insert(2, -251)
print("Test Array(post-insert):" , test_array)