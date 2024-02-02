#BOOLEANS


print(10 > 9) #true
print(10 == 9) #false

print(bool("Hello")) #true_because_nonempty
print(bool(15)) #true_because_nonzero
bool(["apple", "cherry", "banana"]) #true_because_nonempty

class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj)) #return 0

def myFunction() :
  return True
print(myFunction()) #return 1

def myFunction() :
    return True
if myFunction():
    print("YES!")
else:
    print("NO!") #return 1

x = 200
print(isinstance(x, int)) #tocheck_type



#OPERATORS



print(10 + 5) #15

+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y


x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list

x & y #and 
x | y #or
x ^ y #xor
~x    #not
x << 2 #zero fill left shift; for example 3<<2, 3 is 11, and we add 2 0's at the end, we get 1100 is equal to 12(output)
x >> 2 #same as previous, but fills from the right



#LISTS



thislist = ["apple", "banana", "cherry"]
print(thislist)
#outcome: ['apple', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#outcome the count of items

list1 = ["abc", 34, True, 40, "male"] #list can contain different types

mylist = ("apple", "banana", "cherry")
print(type(mylist))  #output is <class 'tuple'>

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)     #also can use list() method

thislist = ["apple", "banana", "cherry"]
print(thislist[1]) #banana

thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) #cherry 

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #["cherry", "orange", "kiwi"]

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) #["apple", "banana", "cherry", "orange"]

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) # ["cherry", "orange", "kiwi", "melon", "mango"]

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) #['apple', 'blackcurrant', 'cherry']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) #['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) #['apple', 'blackcurrant', 'watermelon', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) #['apple', 'watermelon']

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) #['apple', 'banana', 'watermelon', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) #['apple', 'banana', 'cherry', 'orange']   add to the end

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) #['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
#to add list to other, but not only lists, also can other types

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) #['apple', 'cherry']

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist) #delete only first banana

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) #drop the banana

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) #without index, it deletes last one (cherry)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) #drop the apple

thislist = ["apple", "banana", "cherry"]
del thislist #drop full list

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) #deletes content in list, but list still remain

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x) #print all items

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] #short hand for for loop

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1 #with other loop

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)    #add fruits where have letter a and append them into newlist

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) #short newlist = [expression for item in iterable if condition == True]

newlist = [x for x in range(10) if x < 5]

newlist = [x if x != "banana" else "orange" for x in fruits] #if x=banana, we change it to orange

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) #just sort
#thislist.sort(reverse = True) for DESC

def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist) #sort by condition

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) #Capital letters sorted before lower

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) #to ignor the Upper or Lower

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)  #to reverse

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy() #or mylist = list(thislist)
print(mylist) #copy

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)   #merge

for x in list2:
  list1.append(x)
                  #another ways
list1.extend(list2)  



#TUPLES


#A tuple is a collection which is ordered and unchangeable. and allow duplicate values.

thistuple = ("apple",)
print(type(thistuple)) #add comma even if u want to add only one elem

tuple1 = ("abc", 34, True, 40, "male") #also can contain different types

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple) #use tuple() function

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) #to change the tuple convert it to list

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple) #tuple+tuple


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red) #if values<varia put *, and the values will be assigned to the variable as a list



#SEEEEEET


myset = {"apple", "banana", "cherry"}

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) #set function

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)    #to add items

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)     #to delete

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)    #to delete also

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)  #Delete random element

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)     #clean set

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)     #also clean set

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)        #add to sets

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)   #The update() method inserts the items in set2 into set1:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)           #keep only duplicates

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)      #keep uniques

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)       #keep uniques in new 



#DICTIONARY



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
} #key:value pairs
#ordered, changeable and without duplicates

print(thisdict["brand"]) #output:Ford

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

x = thisdict.get("model") #Get the value of the "model" key

x = thisdict.keys() # return a list of all the keys

car["color"] = "white" #add items and change

x = thisdict.values()  #Get a list of the values

x = thisdict.items() #return each item in a dictionary, as tuples in a list.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018 #Change the "year" to 2018

thisdict.update({"year": 2020}) #also to change

del thisdict["model"]
thisdict.pop("model") #to remove

thisdict.popitem() #remove last item 

thisdict.clear()
del thisdict #full drop

for x in thisdict:
  print(x)  #Print all key names

for x in thisdict:
  print(thisdict[x]) #print all values

for x in thisdict.keys():
  print(x)  #output keys with keys()

for x, y in thisdict.items():
  print(x, y)  #output key:value

mydict = thisdict.copy() #copy other dict

mydict = dict(thisdict)
print(mydict) #another way to copy

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}     #dicts in dict



child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}           #create 3 dicts and then add them in 1

print(myfamily["child2"]["name"]) #to access



#IF_ELSE


a = 33
b = 200
if b > a:
    print("b is greater than a") #tab is must have

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal") #elif=else+if

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

if a > b: print("a is greater than b") #short hand if

a = 2
b = 330
print("A") if a > b else print("B") #short hand if-else

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.") #nested if state


a = 33
b = 200
if b > a:
  pass #if statement without content




#WHIIIILE LOOOOOP


i = 1
while i < 6:
  print(i)
  i += 1   #as long as a condition is true.

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1   # stop the loop even if the while condition is true


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)   #skip the iteration

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")  



#FOOOOR_LOOOOOP



fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) #print each element in list

for x in "banana":
  print(x)   #through string

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break     #brake in loop

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)    #skip banana

for x in range(6):
  print(x)    #0 1 2 3 4 5

for x in range(2, 6):
  print(x)    #2 3 4 5 

for x in range(2, 30, 3):
  print(x)    #with 3 step: 2 5 8...29

for x in range(6):
  print(x)
else:
  print("Finally finished!")  #else does after for loop

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")   #If the loop breaks, the else block is not executed.         


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)   #for in for

for x in [0, 1, 2]:
  pass     #if there is no content
