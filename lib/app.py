#Learning data types
#!Strings
str('I am a string')

#The naming convention in python is a  bit different..here you use the snake case naming convention
dog_name = 'Lucy'
#print(dog_name)
#This makes all character to be in uppercase
#print(dog_name.upper())
#This makes all character to be in lowercase
#print(dog_name.lower())
#This only the first letter to be in uppercase
#print(dog_name.capitalize())
#This joins to string together
# print('hello' + 'world')
#This one prints the string by the number of times you tell it to do so
# print('hello' * 3)

#This is the syntax of working with interpolation in python
# print(f"Say hello to my dog {dog_name}")
# price_1 = 3
# price_2 = 2.5
# print(f"Item 1 costs ${price_1:.2f}")
# print(f"Item 1 costs ${price_2:.2f}")

#This is  for checking the type of data you are working on 
# print(type(dog_name))





#!Numbers --> There are two types of numbers integers and floats
#int() and float() --> This both are class constructor functions
#Integers are whole numbers
# print(int('1'))

#Floats are just decimals
# print(float('7.5'))


#!Sequence --> python has different ways of storing data 

#!Lists --> There a couple ways of creating list either using literal constructor or the class constructor
#They are also separated by comma
[1,3,400,7]
print(type([1,3,400,7]))
print(list())
#For list in order to access it you'll need to know its index or position in an element
list_abc = ['a','b','c']
print(list_abc[0])

#There are some list function and methods
##This is used to know the number of elements
len([1,3,400,7])

#This is used to sort them in an ascending order
sorted([5, 100, 234, 7, 2])

list_123 = [1, 2, 3]
#This is the method used to remove the last element
list_123.pop()

#This takes in an argument
list_123.remove(1)
# print(list_123)

#!Tuples --> These are nearly identical to lists,but have tow key differences
#1.They are created using open and close parentheses
# print(type((1,2,3)))

#2 They are immutable  --> They cannot be changed


#!Sets and dicts

#!Sets --> Is un-indexed,un-ordered and unchangeable
# print(set())

#un-indexed --> Meaning we cannot access elements of the set using square brackets
#un-ordered --> Meaning the contents of the set are in a random order
#unchangeable --> Meaning the individual elements cannot be changed

#!Dictionaries --These are composed of keys and values enclosed in curly brackets
my_dict = {"key1": 1, "key2": 2}
#To access data you just use the square brackets notation
my_dict['key2']
#Also you can access it using the get method
print(my_dict.get("key2"))

#!None --> This actually represents the absence of a value
no_value = None
print(no_value)

#!Booleans --> There are only two types tru or false
#not is the operator that reverses the truthy value of a variable
print(not True)
print(not False)


