#booleans ex.1
print(10 > 9)

True
#booleans ex.2
print(10 == 9)

False
#booleans ex.3
print(10 < 9)

False
#booleans ex.4
print(bool("abc"))

True
#booleans ex.5
print(bool(0))

False
#operators ex.1
print(10 * 5)
#operators ex.2
print(10 / 2)
#operators ex.3
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#operators ex.4
if 5 != 10:
  print("5 and 10 is not equal")
#operators ex.5
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")
#lists ex.1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
#lists ex.2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
#lists ex.3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
#lists ex.4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
#lists ex.5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
#lists ex.6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
#lists ex.7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
#lists ex.8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))
#turples ex.1
fruits = ("apple", "banana", "cherry")
print(fruits[0])
#turples ex.2
fruits = ("apple", "banana", "cherry")
print(len(fruits))
#turples ex.3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])
#turples ex.4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])
#sets ex.1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#sets ex.2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
#sets ex.3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
#sets ex.4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
#sets ex.5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
#dictionaries ex.1
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
#dictionaries ex.2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
#dictionaries ex.3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
#dictionaries ex.4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
#dictionaries ex.5
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
#If...else ex.1
a = 50
b = 10
if a > b:
  print("Hello World")
#If...else ex.2
a = 50
b = 10
if a != b:
  print("Hello World")
#If...else ex.3
a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")
#If...else ex.4
a = 50
b = 10
if a == b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")
#If...else ex.5
if a == b and c == d:
  print("Hello")
#If...else ex.6
if a == b or c == d:
  print("Hello")
#If...else ex.7
if 5 > 2:
  print("Five is greater than two!")
#If...else ex.8
if 5 > 2: print("Five is greater than two!")
#If...else ex.9
print("Yes") if 5 > 2 else print("No")
#While loop ex.1
i = 1
while i < 6:
  print(i)
  i += 1
#While loop ex.2
i = 1
while i < 6:
  if i == 3:
    break
  i += 1
#While loop ex.3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#While loop ex.4
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
#For loop ex.1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#For loop ex.2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#For loop ex.3
for x in range(6):
  print(x)
#For loop ex.4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)