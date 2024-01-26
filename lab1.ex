#example_conditions 
if 5 > 2:
  print("Five is greater than two!")
if 5 > 2:
        print("Five is greater than two!") 
        
#example_create_variable
x = 5
y = "Hello, World!" 
print(x)
print(y) 

#example_of_comments
#This is a comment
#This is a comment
#written in
#more than just one line
"""
This is a comment
written in
more than just one line
"""

#example_x_changes_type
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#example_casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#example_take_type
x = 5
y = "John"
print(type(x))
print(type(y))

#example_single_double_aresame
x = "John"
# is the same as
x = 'John'

#example_Aa_diff
a = 4
A = "Sally"
#A will not overwrite a

#example_legal_names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
#example_ManyValues
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#example_same
x = y = z = "Orange"
print(x)
print(y)
print(z)
#example_list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#example_output
x = "Python is awesome"
print(x)
#or
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#or 
print(x + y + z)

#example_globalVariable
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()
#example
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc() #output is fantastic

#example_global_vari
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
#also we can change variable inside the def
x = "awesome"
def myfunc():
  global x
  x = "fantastic"

#example_numeric_data_types
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#example_convert from int to float:
x = 1    # int
a = float(x)
#but we can't convert complex to another

#example_random_number
import random
print(random.randrange(1, 10))

#example_Specify_a_VariableType
x = float(1)     # x will be 1.0
y = int(2.8) # y will be 2
z = str(3.0)  # z will be '3.0'

#example_mulriline_string 
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#example_strings_as_arrays
a = "Hello, World!"
print(a[1])
for x in "banana":
  print(x)
  
#take_length
a = "Hello, World!"
print(len(a))

#Example_Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt) #is true
txt = "The best things in life are free!"
print("expensive" not in txt) #isfalse

#example_getCharaFromStr
b = "Hello, World!"
print(b[2:5]) #from 2 to 5
b = "Hello, World!"
print(b[:5]) #from start to 5(not included)
b = "Hello, World!"
print(b[2:]) #from 2 to end
b = "Hello, World!"
print(b[-5:-2]) #from "o" in "World!" to  "d" in "World!"

#example_to_modifyStr
print(a.upper()) #toUpperCase
print(a.lower()) #toLowerCase
print(a.strip()) #DeleteSpacesFromBeginAndEnd
print(a.replace("H", "J")) #replaceWithOtherStr
print(a.split(",")) #split the string at the places we have ","

#example_format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#we can use indexes to put in correct order
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#if u wanna put word with "", should surround with /
txt = "We are the so-called \"Vikings\" from the north."
#OTHERS 
# \'	Single Quote
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value
