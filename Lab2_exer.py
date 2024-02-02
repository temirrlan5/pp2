#BOOLEAN
#ex1
print(10 > 9)
True
#ex2
print(10 == 9)
False
#ex3
print(10 < 9)
False
#ex4
print(bool("abc"))
True
#ex5
print(bool(0))
False


#OPERATORS
#ex1
print(10 *5)
#ex2
print(10 /2)
#ex3
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#ex4
if 5!=10:
  print("5 and 10 is not equal")
#ex5
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")


#LISTS
#ex1  
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
#ex2
fruits = ["apple", "banana", "cherry"]
fruits[0]="kiwi"
#ex3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
#ex4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")
#ex5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
#ex6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
#ex7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
#ex8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))


#TUPLES
#ex1  
fruits = ("apple", "banana", "cherry")
print(fruits[0])
#ex2
fruits = ("apple", "banana", "cherry")
print(len(fruits))
#ex3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])
#ex4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])


#SEEETS
#ex1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#ex2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
#ex3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
#ex4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
#ex5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")


#DICTIONARY
#ex1
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
#ex2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"]=2020
#ex3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"]="red"
#ex4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
#ex5
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()


#IF_ELSE
#ex1
a = 50
b = 10
if a>b:
    print("Hello World")
#ex2
a = 50
b = 10
if a!=b: 
    print("Hello World")
#ex3
a = 50
b = 10
if a==b:
    print("Yes")
else:
    print("No")
#ex4
a = 50
b = 10
if a==b:
  print("1")
elif a>b:
  print("2")
else:
  print("3")
#ex5
if a == b and c == d:
  print("Hello")
#ex6
if a == b or c == d:
  print("Hello")
#ex7
if 5 > 2:
    print("YES")
#ex8
a = 2
b = 5
print("YES") if a == b else print("NO")
#ex9
a = 2
b = 50
c = 2
if a == c or b == c:
  print("YES")


#WHILE_LOOP
#ex1
i = 1
while i < 6:
    print(i)
    i += 1
#ex2
i = 1
while i < 6:
  if i == 3:
    break
  i += 1
#ex3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#ex4  
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


#FOR_LOOOOP
#ex1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#ex2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#ex3
for x in range(6):
  print(x)
#ex4  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
